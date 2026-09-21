# Main execution script for the Python Monitoring System (PMS).
# Integrates data collection, export handlers, the plotting engine, and the web dashboard.

import time

from modules.collector import SystemCollector
from modules.exporter import Exporter
from modules.plotter import MetricsPlotter
from modules.web_interface import WebDashboard

SAMPLE_INTERVAL_SECONDS = 5


def run_system() -> None:
    # Initializes and runs all primary PMS modules

    # core components
    collector = SystemCollector()
    exporter = Exporter(output_directory="logs")
    plotter = MetricsPlotter(theme="dark")
    dashboard = WebDashboard(host="127.0.0.1", port=8080, metrics_provider=collector.collect_all)

    # dashboard service
    dashboard.start_server()
    print(f"Dashboard running at {dashboard.get_status_context()['url']}")

    # monitoring loop: samples metrics, mirrors them to the dashboard, and logs them to disk
    try:
        while True:
            snapshot = collector.collect_all()
            chart_data = plotter.generate_chart_payload("CPU_Load", [snapshot["cpu_percent"]])

            exporter.save_json(filename="latest_snapshot.json", data=snapshot)
            exporter.save_log(
                filename="system_summary.txt",
                data=f"Monitoring Status: {dashboard.get_status_context()}\nPayload: {chart_data}",
            )

            time.sleep(SAMPLE_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        dashboard.stop_server()


if __name__ == "__main__":
    run_system()