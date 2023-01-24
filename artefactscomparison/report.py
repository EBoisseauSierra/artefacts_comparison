"""This modules defines the Report class."""

from __future__ import annotations

from .compare import (
    FilepathCollection,
    FilepathMapping,
    list_added_files,
    list_deleted_files,
    list_renamed_files,
    list_untouched_files,
)
from .csv_parser import ContentToFilepathMapping


class Report:
    """A report on the artefacts differences between base and head."""

    def __init__(
        self, base: ContentToFilepathMapping, head: ContentToFilepathMapping
    ) -> None:
        """Instantiate Report."""
        self.base = base
        self.head = head

    def generate(self) -> Report:
        """Generate report.

        Populate the Report object with the list/mapping of added, deleted,
        renamed, and untouched artifacts between base and head.

        Returns:
            Report: A populated report.
        """
        self.added_artefacts = list_added_files(self.base, self.head)
        self.deleted_artefacts = list_deleted_files(self.base, self.head)
        self.renamed_artefacts = list_renamed_files(self.base, self.head)
        self.untouched_artefacts = list_untouched_files(self.base, self.head)

        return self

    def to_str(self) -> str:
        """Get a text version of the report.

        Returns:
            str: Report formatted as a Markdown diff code snippet.
        """
        report = ["```diff"]

        if self.added_artefacts:
            report.append(
                f"@@ {self._print_artefacts_count(self.added_artefacts)} added @@"
            )
            for filename in sorted(self.added_artefacts):
                report.append(f"+ {filename}")
            report.append("")

        if self.deleted_artefacts:
            report.append(
                f"@@ {self._print_artefacts_count(self.deleted_artefacts)} deleted @@"
            )
            for filename in sorted(self.deleted_artefacts):
                report.append(f"- {filename}")
            report.append("")

        if self.renamed_artefacts:
            report.append(
                f"@@ {self._print_artefacts_count(self.renamed_artefacts)} renamed @@"
            )
            for old_filename, new_filename in sorted(self.renamed_artefacts.items()):
                report.append(f"! {old_filename} ￫ {new_filename}")
            report.append("")

        if self.untouched_artefacts:
            artefacts_count = self._print_artefacts_count(
                self.renamed_artefacts,
                add_other=self.added_artefacts
                or self.deleted_artefacts
                or self.renamed_artefacts,
            )
            report.append(f"# {artefacts_count} remain unmodified")

        report.append("```")

        return "\n".join(report)

    @staticmethod
    def _print_artefacts_count(
        filepaths: FilepathCollection | FilepathMapping,
        add_other: bool = False,
    ) -> str:
        """Beautify the count of artefacts, adding plural when necessary.

        Args:
            filepaths (FilepathCollection | FilepathMapping): List/mapping of
                artefacts to count.
            add_other (bool, optional): Whether to add 'other' between the
                count of file and the string 'file(s)'. Defaults to False.

        Returns:
            str: Nicely formatted sting counting the artefacts in the
                collection.
        """
        if not filepaths:
            return ""
        if len(filepaths) == 1:
            return "1 other file" if add_other else "1 file"
        return (
            f"{len(filepaths)} other files" if add_other else f"{len(filepaths)} files"
        )
