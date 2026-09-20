"""
web_interface.py
----------------
Manages web dashboard routes, HTTP controllers, and live metric endpoints.
"""

from typing import Dict, Any


class WebDashboard:
    """HTTP web server controller for live system monitoring visualization."""

    def __init__(self, host: str = "127.0.0.1", port: int = 8080) -> None:
        self.host = host
        self.port = port
        self.is_running = False

    def start_server(self) -> None:
        """Starts the dashboard HTTP server daemon."""
        self.is_running = True

    def get_status_context(self) -> Dict[str, Any]:
        """Provides the current web dashboard status context."""
        return {
            "server_status": "active" if self.is_running else "inactive",
            "url": f"http://{self.host}:{self.port}",
        }