# Python Monitoring System (PMS)

A lightweight, modular Python system monitoring tool designed to collect real-time hardware metrics (CPU, RAM, Disk), generate evaluations, export log files, and serve a web interface.

---

## 🚀 Features

- **Real-Time Metric Collection**: Monitors CPU usage, RAM utilization, and disk space using `psutil`.
- **Modular Architecture**: Clean separation of data collection, visualization, export, and web interface adhering to PEP 8.
- **Text & JSON Export**: Logs system states as plain text and exports metric snapshots to `.json` files.
- **Live Web Dashboard**: Built-in HTTP server rendering the dashboard template and serving metrics via a `/api/metrics` endpoint, polled by the page every few seconds.
- **Automated Testing**: Core module functionality covered via `pytest`.

---

## 📁 Project Structure

```text
pms_project/
├── modules/
│   ├── __init__.py
│   ├── collector.py        # Gathers system metrics (psutil)
│   ├── plotter.py           # Data processing & chart payloads
│   ├── exporter.py         # Text and JSON log/export handlers
│   └── web_interface.py    # Web server & dashboard controller
├── templates/
│   └── test_dashboard.html # HTML/CSS/JS dashboard template
├── test/
│   └── test_pms.py         # Automated unit tests
├── main.py                 # Main application entry point
├── requirements.txt        # Dependency list
└── README.md               # Project documentation
```

---

## 🛠️ Installation

### Prerequisites
- Python 3.9 or higher

### Step-by-Step Setup

1. **Clone or download the repository**:
```bash
git clone https://github.com/jesajaw/PMS
cd PMS
```
2. **Create and activate a virtual environment**:
```bash
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```

---

## 💻 Usage
### Run the Main Application
Execute `main.py` to start the monitoring loop and the web dashboard:
```bash
python main.py
```
The dashboard is then reachable at `http://127.0.0.1:8080`.

### Run Tests
Verify that all modules function correctly:
```bash
pytest
```

---

## 🧱 Module Overview

| Module | Description |
| :--- | :--- |
| `main.py` | Orchestrates the primary execution flow, starts the web dashboard, and periodically logs metrics. |
| `modules/collector.py` | Retrieves hardware metrics (CPU, RAM, Disk) using `psutil`. |
| `modules/plotter.py` | Handles charting themes and structures metric data payloads. |
| `modules/exporter.py` | Creates log directories and exports evaluations to `.txt` and `.json` files. |
| `modules/web_interface.py` | Runs the dashboard HTTP server and serves live metric data to the browser. |
