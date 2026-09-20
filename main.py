"""
main.py
-------
Main execution script for the Python Monitoring System (PMS).
Integrates export handlers, plotting engines, and web dashboard instances.
"""

from modules.txt_exporter import TextExporter
from modules.plotter import MetricsPlotter
from modules.web_interface import WebDashboard


def run_system() -> None:
    """Initializes and runs all primary PMS modules."""
    # Instantiate core components
    exporter = TextExporter(output_directory="logs")
    plotter = MetricsPlotter(theme="dark")
    dashboard = WebDashboard(host="127.0.0.1", port=8080)

    # Start dashboard service
    dashboard.start_server()

    # Sample execution pipeline
    sample_cpu_load = [12.4, 35.8, 42.1, 28.9]
    chart_data = plotter.generate_chart_payload("CPU_Load", sample_cpu_load)
    
    # Save monitoring summary
    exporter.save_log(
        filename="system_summary.txt",
        data=f"Monitoring Status: {dashboard.get_status_context()}\nPayload: {chart_data}"
    )


if __name__ == "__main__":
    run_system()