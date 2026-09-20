# Python Monitoring System (PMS)

A lightweight, modular Python system monitoring tool designed to collect real-time hardware metrics (CPU, RAM, Disk), generate evaluations, export log files, and serve a web interface.

---

## 🚀 Features

- **Real-Time Metric Collection**: Monitors CPU usage, RAM utilization, and disk space using `psutil`.
- **Modular Architecture**: Clean separation of data collection, visualization, export, and web interface adhering to PEP 8.
- **Text Export**: Automatically logs system states and performance metrics to plain text files.
- **Web Dashboard**: Modern HTML template for visualizing system metrics directly in the browser.
- **Automated Testing**: Core module functionality covered via `pytest`.

---

## 📁 Project Structure

```text
pms_project/
├── modules/
│   ├── __init__.py
│   ├── collector.py        # Gathers system metrics (psutil)
│   ├── plotter.py           # Data processing & chart payloads
│   ├── txt_exporter.py     # Log and file export handlers
│   └── web_interface.py    # Web server & dashboard controller
├── templates/
│   └── test_dashboard.html # HTML/CSS dashboard template
├── tests/
│   └── test_pms.py         # Automated unit tests
├── main.py                 # Main application entry point
├── pyproject.toml          # Package and dependency configuration
└── README.md               # Project documentation
```
## 🛠️ Installation

### Prerequisites
- Python 3.9 or higher

### Step-by-Step Setup

1. **Clone or download the repository**:
```bash
git clone [https://github.com/user/pms_project.git](https://github.com/user/pms_project.git)
cd pms_project
```
2. **Create and activate a virtual environment (recommended)**:
```bash
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```
3. Install the package and dependencies:
```bash
# Standard installation
pip install .

# Development installation (includes pytest & linters)
pip install -e .[dev]
```

## 💻 Usage
### Run the Main Application
Execute `main.py` to initialize and run the monitoring system:
```bash
python main.py
```
### Run Tests
Verify that all modules function correctly:
```bash
pytest
```

## 🧱 Module Overview

| Module | Description |
| :--- | :--- |
| `main.py` | Orchestrates the primary execution flow, starts the web interface, and logs initial metrics. |
| `modules/collector.py` | Retrieves hardware metrics (CPU, RAM, Disk) using `psutil`. |
| `modules/plotter.py` | Handles charting themes and structures metric data payloads. |
| `modules/txt_exporter.py` | Creates log directories and exports evaluations to text files. |
| `modules/web_interface.py` | Manages web server states and serves metric data to the dashboard. |