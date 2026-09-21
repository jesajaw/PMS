from pathlib import Path
from modules import Exporter, MetricsPlotter, SystemCollector, WebDashboard


def test_txt_exporter(tmp_path: Path) -> None:
    exporter = Exporter(output_directory=tmp_path)
    output_file = exporter.save_log("test.txt", "Sample Log Line")

    assert output_file.exists()
    assert output_file.read_text(encoding="utf-8") == "Sample Log Line"


def test_json_exporter(tmp_path: Path) -> None:
    exporter = Exporter(output_directory=tmp_path)
    output_file = exporter.save_json("test.json", {"cpu_percent": 12.4})

    assert output_file.exists()
    assert '"cpu_percent": 12.4' in output_file.read_text(encoding="utf-8")


def test_plotter_payload() -> None:
    plotter = MetricsPlotter(theme="dark")
    payload = plotter.generate_chart_payload("RAM", [50.0, 55.0, 60.0])

    assert payload["title"] == "RAM"
    assert payload["sample_count"] == 3


def test_system_collector() -> None:
    snapshot = SystemCollector().collect_all()

    assert set(snapshot.keys()) == {"cpu_percent", "ram_percent", "disk_percent"}
    assert all(isinstance(value, float) for value in snapshot.values())


def test_web_interface_status() -> None:
    dashboard = WebDashboard()
    assert dashboard.get_status_context()["server_status"] == "inactive"

    dashboard.start_server()
    assert dashboard.get_status_context()["server_status"] == "active"
    dashboard.stop_server()
    assert dashboard.get_status_context()["server_status"] == "inactive"