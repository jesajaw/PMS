from typing import Dict, List, Union, Any


class MetricsPlotter:
    # generates graphic visualizations and chart configurations for metric data, in this case system performance visualizer
    def __init__(self, theme: str = "default") -> None:
        self.theme = theme

    def generate_chart_payload(self, metric_name: str, values: List[Union[int, float]]) -> Dict[str, Any]: # formats data points into chart rendering payload
        # `metric_name` : identifier for the plotted metric ('CPU_Usage',...)
        # `values` : numerical series data to plot
        # returns a structured chart payload dictionary
        return {
            "title": metric_name,
            "theme": self.theme,
            "data_points": values,
            "sample_count": len(values),
        }