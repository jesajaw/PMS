# handles writing and exporting system monitoring metrics to text and JSON files.

import json
from pathlib import Path
from typing import Any, List, Union


class Exporter:# Utility class for saving log strings, metric lists, and structured data to files

    def __init__(self, output_directory: Union[str, Path] = "logs") -> None:
        self.output_dir = Path(output_directory)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def save_log(self, filename: str, data: Union[str, List[str]]) -> Path: # writes content to a specified text file in the output directory
        # filename: Name of the target file
        # data: Text content or list of log lines to write
        # return: Path to the generated text file

        file_path = self.output_dir / filename
        content = "\n".join(data) if isinstance(data, list) else data

        with open(file_path, mode="w", encoding="utf-8") as file:
            file.write(content)

        return file_path

    def save_json(self, filename: str, data: Any) -> Path: # writes a JSON-serializable object to the output directory
        # `filename` : name of the target .json file
        # `data` : any JSON-serializable object (dict, list, ...)
        # returns the path to the generated file
        file_path = self.output_dir / filename

        with open(file_path, mode="w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

        return file_path