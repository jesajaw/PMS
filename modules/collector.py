"""
collector.py
------------
Gathers live system performance metrics (CPU, RAM, Disk).
"""

from typing import Dict, Any
import psutil


class SystemCollector:
    """Collects current hardware performance indicators."""

    @staticmethod
    def get_cpu_usage() -> float:
        """Returns current CPU utilization percentage."""
        return psutil.cpu_percent(interval=0.5)

    @staticmethod
    def get_ram_usage() -> float:
        """Returns RAM usage percentage."""
        return psutil.virtual_memory().percent

    @staticmethod
    def get_disk_usage() -> float:
        """Returns primary disk usage percentage."""
        return psutil.disk_usage("/").percent

    def collect_all(self) -> Dict[str, Any]:
        """Gathers a combined snapshot of all system metrics."""
        return {
            "cpu_percent": self.get_cpu_usage(),
            "ram_percent": self.get_ram_usage(),
            "disk_percent": self.get_disk_usage(),
        }