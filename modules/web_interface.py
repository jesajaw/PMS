# manages web dashboard routes, HTTP controllers, and live metric endpoints

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Callable, Dict, Optional

TEMPLATES_DIR = Path(__file__).resolve().parent.parent / "templates"
DASHBOARD_TEMPLATE = TEMPLATES_DIR / "test_dashboard.html"


class _DashboardRequestHandler(BaseHTTPRequestHandler):
    # translates incoming HTTP requests into dashboard responses; metrics_provider is injected by WebDashboard

    metrics_provider: Optional[Callable[[], Dict[str, Any]]] = None

    def do_GET(self) -> None: # routes GET requests to the dashboard page or the metrics API
        if self.path in ("/", "/index.html"):
            self._serve_dashboard()
        elif self.path == "/api/metrics":
            self._serve_metrics()
        else:
            self.send_error(404, "Not Found")

    def _serve_dashboard(self) -> None: # returns the static dashboard HTML page
        try:
            html = DASHBOARD_TEMPLATE.read_text(encoding="utf-8")
        except FileNotFoundError:
            self.send_error(500, "Dashboard template missing")
            return

        body = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _serve_metrics(self) -> None: # returns the latest metric snapshot as JSON
        metrics = self.metrics_provider() if self.metrics_provider else {}
        body = json.dumps(metrics).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: Any) -> None: # silences the default request logging to stderr
        pass


class WebDashboard:
    # HTTP web server controller for live system monitoring visualization

    def __init__(self, host: str = "127.0.0.1", port: int = 8080,
                 metrics_provider: Optional[Callable[[], Dict[str, Any]]] = None) -> None:
        self.host = host
        self.port = port
        self.metrics_provider = metrics_provider
        self.is_running = False

        self._server: Optional[ThreadingHTTPServer] = None
        self._server_thread: Optional[threading.Thread] = None

    def start_server(self) -> None: # starts the dashboard HTTP server as a background daemon thread
        if self.is_running:
            return

        handler = type("BoundDashboardHandler", (_DashboardRequestHandler,),
                        {"metrics_provider": staticmethod(self.metrics_provider or (lambda: {}))})

        self._server = ThreadingHTTPServer((self.host, self.port), handler)
        self._server_thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        self._server_thread.start()
        self.is_running = True

    def stop_server(self) -> None: # shuts down the dashboard HTTP server
        if not self.is_running or self._server is None:
            return

        self._server.shutdown()
        self._server.server_close()
        self.is_running = False

    def get_status_context(self) -> Dict[str, Any]: # provides the current web dashboard status context
        return {
            "server_status": "active" if self.is_running else "inactive",
            "url": f"http://{self.host}:{self.port}",
        }