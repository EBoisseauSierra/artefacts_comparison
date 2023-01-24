from artefactscomparison.report import Report

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

report = Report(base=base, head=head)


def test_Report_generate():
    report.generate()

    added_artefacts_expected = [
        "added_1",
        "added_2",
        "added_3",
    ]
    assert len(report.added_artefacts) == len(added_artefacts_expected)
    assert set(report.added_artefacts) == set(added_artefacts_expected)

    assert report.renamed_artefacts == {
        "to_rename_1": "renamed_1",
        "to_rename_2": "renamed_2",
    }

    assert report.deleted_artefacts == ["to_be_deleted"]

    untouched_artefacts_expected = [
        "no_change_1",
        "no_change_2",
        "no_change_3",
        "no_change_4",
    ]
    assert len(report.untouched_artefacts) == len(untouched_artefacts_expected)
    assert set(report.untouched_artefacts) == set(untouched_artefacts_expected)


def test_Report_print_artefacts_count_when_no_file_list():
    assert report._print_artefacts_count([]) == ""


def test_Report_print_artefacts_count_when_no_file_dict():
    assert report._print_artefacts_count({}) == ""


def test_Report_print_artefacts_count_when_no_file_list_and_other():
    assert report._print_artefacts_count([], add_other=True) == ""


def test_Report_print_artefacts_count_when_no_file_dict_and_other():
    assert report._print_artefacts_count({}, add_other=True) == ""


def test_Report_print_artefacts_count_when_one_file_list():
    assert report._print_artefacts_count(["foo"]) == "1 file"


def test_Report_print_artefacts_count_when_one_file_dict():
    assert report._print_artefacts_count({"foo": "bar"}) == "1 file"


def test_Report_print_artefacts_count_when_one_file_list_and_other():
    assert report._print_artefacts_count(["foo"], add_other=True) == "1 other file"


def test_Report_print_artefacts_count_when_one_file_dict_and_other():
    assert (
        report._print_artefacts_count({"foo": "bar"}, add_other=True) == "1 other file"
    )


def test_Report_print_artefacts_count_when_multiple_files_list():
    assert report._print_artefacts_count(["foo", "bar", "baz"]) == "3 files"


def test_Report_print_artefacts_count_when_multiple_files_dict():
    assert (
        report._print_artefacts_count({"foo": "bar", "baz": "buzz", "biz": "boz"})
        == "3 files"
    )


def test_Report_print_artefacts_count_when_multiple_files_list_and_other():
    assert (
        report._print_artefacts_count(["foo", "bar", "baz"], add_other=True)
        == "3 other files"
    )


def test_Report_print_artefacts_count_when_multiple_files_dict_and_other():
    assert (
        report._print_artefacts_count(
            {"foo": "bar", "baz": "buzz", "biz": "boz"}, add_other=True
        )
        == "3 other files"
    )
