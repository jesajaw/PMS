"""
txt_exporter.py
---------------
Handles writing and exporting system monitoring metrics to plain text files.
"""

from pathlib import Path
from typing import List, Union


class TextExporter:
    """Utility class for saving log strings and metric lists to text files."""

    def __init__(self, output_directory: Union[str, Path] = "logs") -> None:
        self.output_dir = Path(output_directory)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def save_log(self, filename: str, data: Union[str, List[str]]) -> Path:
        """Writes content to a specified text file in the output directory.

        :param filename: Name of the target file.
        :param data: Text content or list of log lines to write.
        :return: Path to the generated text file.
        """
        file_path = self.output_dir / filename
        content = "\n".join(data) if isinstance(data, list) else data

        with open(file_path, mode="w", encoding="utf-8") as file:
            file.write(content)

        return file_path