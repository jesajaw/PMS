"""
plotter.py
----------
Generates graphic visualizations and chart configurations for metric data.
"""

from typing import Dict, List, Union, Any


class MetricsPlotter:
    """Renders charts and data configurations for system performance visualizer."""

    def __init__(self, theme: str = "default") -> None:
        self.theme = theme

    def generate_chart_payload(self, metric_name: str, values: List[Union[int, float]]) -> Dict[str, Any]:
        """Formats data points into a chart rendering payload.

        :param metric_name: Identifier for the plotted metric (e.g., 'CPU_Usage').
        :param values: Numerical series data to plot.
        :return: Structured chart payload dictionary.
        """
        return {
            "title": metric_name,
            "theme": self.theme,
            "data_points": values,
            "sample_count": len(values),
        }