"""
test_pms.py
-----------
Unit tests for the Python Monitoring System modules.
"""

from pathlib import Path
import pytest

from modules.txt_exporter import TextExporter
from modules.plotter import MetricsPlotter
from modules.web_interface import WebDashboard


def test_txt_exporter(tmp_path: Path) -> None:
    exporter = TextExporter(output_directory=tmp_path)
    output_file = exporter.save_log("test.txt", "Sample Log Line")

    assert output_file.exists()
    assert output_file.read_text(encoding="utf-8") == "Sample Log Line"


def test_plotter_payload() -> None:
    plotter = MetricsPlotter(theme="dark")
    payload = plotter.generate_chart_payload("RAM", [50.0, 55.0, 60.0])

    assert payload["title"] == "RAM"
    assert payload["sample_count"] == 3


def test_web_interface_status() -> None:
    dashboard = WebDashboard()
    assert dashboard.get_status_context()["server_status"] == "inactive"

    dashboard.start_server()
    assert dashboard.get_status_context()["server_status"] == "active"