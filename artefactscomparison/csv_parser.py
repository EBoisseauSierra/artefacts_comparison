"""This modules contains utility to parse an artefact summary."""

import csv
from pathlib import Path
from typing import TypeAlias

# A dict mapping the content of a file (represented as its SHA sum)
# to its file path
ContentToFilepathMapping: TypeAlias = dict[str, str]


def get_content_to_filepath_mapping(
    path: Path | str,
) -> ContentToFilepathMapping:
    """Parse an artefact summary and return a mapping of artefacts' content to path.

    Args:
        path (Path | str): Path to a CSV file containing an artefact summary.

    Returns:
        ContentToFilepathMapping: Mapping of the artefacts' content (as a SHA
        sum) to its file path.
    """
    with open(path, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        next(reader)  # Skip CSV header
        content_to_filepath_mapping = {str(row[0]): str(row[1]) for row in reader}

    return content_to_filepath_mapping
