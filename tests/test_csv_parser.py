from io import StringIO
from unittest.mock import mock_open, patch

from artefactscomparison.csv_parser import get_content_to_filepath_mapping

# Note: We have dropped header from mocked artefact summary — not so sure why it doesn't
# work with them.

empty_artefact_summary = StringIO(
    """
"""
).getvalue()


def test_get_content_to_filepath_mapping_when_empty_summary():
    with patch(
        "builtins.open", mock_open(read_data=empty_artefact_summary)
    ) as mock_file:
        assert get_content_to_filepath_mapping(mock_file) == {}


populated_artefact_summary = StringIO(
    """
1,no_change_1
2,no_change_2
3,no_change_3
4,no_change_4
5,to_rename_1
6,to_rename_2
7,to_be_deleted
"""
).getvalue()


def test_get_content_to_filepath_mapping_when_populated_summary():
    with patch(
        "builtins.open", mock_open(read_data=populated_artefact_summary)
    ) as mock_file:
        assert get_content_to_filepath_mapping(mock_file) == {
            "1": "no_change_1",
            "2": "no_change_2",
            "3": "no_change_3",
            "4": "no_change_4",
            "5": "to_rename_1",
            "6": "to_rename_2",
            "7": "to_be_deleted",
        }
