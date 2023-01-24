from artefactscomparison.compare import (
    list_added_files,
    list_deleted_files,
    list_renamed_files,
    list_untouched_files,
)


def test_list_added_files_when_no_added_file():
    base = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "5": "to_rename_1",
        "6": "to_rename_2",
        "7": "to_be_deleted",
    }
    head = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "5": "renamed_1",
        "6": "renamed_2",
    }
    assert list_added_files(base, head) == []


def test_list_added_files_when_one_added_file():
    base = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "5": "to_rename_1",
        "6": "to_rename_2",
        "7": "to_be_deleted",
    }
    head = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "5": "renamed_1",
        "6": "renamed_2",
        "8": "added_1",
    }
    assert list_added_files(base, head) == [
        "added_1",
    ]


def test_list_added_files_when_multiple_added_files():
    base = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "5": "to_rename_1",
        "6": "to_rename_2",
        "7": "to_be_deleted",
    }
    head = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "5": "renamed_1",
        "6": "renamed_2",
        "8": "added_1",
        "9": "added_2",
        "10": "added_3",
    }

    added_filenames_expected = ["added_1", "added_2", "added_3"]
    added_filenames_computed = list_added_files(base, head)

    # Same length
    assert len(added_filenames_computed) == len(added_filenames_expected)
    # Same content, irrespective of order
    assert set(added_filenames_computed) == set(added_filenames_expected)


def test_list_deleted_files_when_no_deleted_file():
    base = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "5": "to_rename_1",
        "6": "to_rename_2",
    }
    head = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "5": "renamed_1",
        "6": "renamed_2",
        "8": "added_1",
        "9": "added_2",
        "10": "added_3",
    }
    assert list_deleted_files(base, head) == []


def test_list_deleted_files_when_one_deleted_file():
    base = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "5": "to_rename_1",
        "6": "to_rename_2",
        "7": "to_be_deleted",
    }
    head = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "5": "renamed_1",
        "6": "renamed_2",
        "8": "added_1",
        "9": "added_2",
        "10": "added_3",
    }
    assert list_deleted_files(base, head) == [
        "to_be_deleted",
    ]


def test_list_deleted_files_when_multiple_deleted_files():
    base = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "5": "to_rename_1",
        "6": "to_rename_2",
        "71": "to_be_deleted_1",
        "72": "to_be_deleted_2",
        "73": "to_be_deleted_3",
    }
    head = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "5": "renamed_1",
        "6": "renamed_2",
        "8": "added_1",
        "9": "added_2",
        "10": "added_3",
    }

    deleted_filenames_expected = [
        "to_be_deleted_1",
        "to_be_deleted_2",
        "to_be_deleted_3",
    ]
    deleted_filenames_computed = list_deleted_files(base, head)

    # Same length
    assert len(deleted_filenames_computed) == len(deleted_filenames_expected)
    # Same content, irrespective of order
    assert set(deleted_filenames_computed) == set(deleted_filenames_expected)


def test_list_renamed_files_when_no_renamed_file():
    base = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "7": "to_be_deleted",
    }
    head = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "8": "added_1",
        "9": "added_2",
        "10": "added_3",
    }
    assert list_renamed_files(base, head) == {}


def test_list_renamed_files_when_one_renamed_file():
    base = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "5": "to_rename_1",
        "7": "to_be_deleted",
    }
    head = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "5": "renamed_1",
        "8": "added_1",
        "9": "added_2",
        "10": "added_3",
    }
    assert list_renamed_files(base, head) == {"to_rename_1": "renamed_1"}


def test_list_renamed_files_when_multiple_renamed_files():
    base = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "5": "to_rename_1",
        "6": "to_rename_2",
        "61": "to_rename_3",
        "7": "to_be_deleted",
    }
    head = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "5": "renamed_1",
        "6": "renamed_2",
        "61": "renamed_3",
        "8": "added_1",
        "9": "added_2",
        "10": "added_3",
    }

    assert list_renamed_files(base, head) == {
        "to_rename_1": "renamed_1",
        "to_rename_2": "renamed_2",
        "to_rename_3": "renamed_3",
    }


def test_list_untouched_files_when_no_untouched_file():
    base = {
        "5": "to_rename_1",
        "6": "to_rename_2",
        "7": "to_be_deleted",
    }
    head = {
        "5": "renamed_1",
        "6": "renamed_2",
        "8": "added_1",
        "9": "added_2",
        "10": "added_3",
    }
    assert list_untouched_files(base, head) == []


def test_list_untouched_files_when_one_untouched_file():
    base = {
        "1": "no_change_1",
        "5": "to_rename_1",
        "6": "to_rename_2",
        "7": "to_be_deleted",
    }
    head = {
        "1": "no_change_1",
        "5": "renamed_1",
        "6": "renamed_2",
        "8": "added_1",
        "9": "added_2",
        "10": "added_3",
    }
    assert list_untouched_files(base, head) == [
        "no_change_1",
    ]


def test_list_untouched_files_when_multiple_untouched_files():
    base = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "5": "to_rename_1",
        "6": "to_rename_2",
        "7": "to_be_deleted",
    }
    head = {
        "1": "no_change_1",
        "2": "no_change_2",
        "3": "no_change_3",
        "4": "no_change_4",
        "5": "renamed_1",
        "6": "renamed_2",
        "8": "added_1",
        "9": "added_2",
        "10": "added_3",
    }

    untouched_filenames_expected = [
        "no_change_1",
        "no_change_2",
        "no_change_3",
        "no_change_4",
    ]
    untouched_filenames_computed = list_untouched_files(base, head)

    # Same length
    assert len(untouched_filenames_computed) == len(untouched_filenames_expected)
    # Same content, irrespective of order
    assert set(untouched_filenames_computed) == set(untouched_filenames_expected)
