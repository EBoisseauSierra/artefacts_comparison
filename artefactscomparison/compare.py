"""This module contains utilities to compare artefact summaries."""

from typing import TypeAlias

from .csv_parser import ContentToFilepathMapping

# Relative file path to an artefact
Filepath: TypeAlias = str

# List of artefacts' file paths
FilepathCollection: TypeAlias = list[Filepath]

# Mapping of old to new artefacts' file paths (i.e. former path
# to renamed path)
FilepathMapping: TypeAlias = dict[Filepath, Filepath]


def list_untouched_files(
    base: ContentToFilepathMapping, head: ContentToFilepathMapping
) -> FilepathCollection:
    """List artefacts untouched between base and head.

    This means that neither the content nor the file path varies between base and head.

    Args:
        base (ContentToFilepathMapping): Mapping of artefacts content to their
            filename in the base summary.
        head (ContentToFilepathMapping): Mapping of artefacts content to their
            filename in the head summary.

    Returns:
        FilepathCollection: List of file paths of artefacts for which neither
            the content nor the file path varies between base and head.
    """
    # List contents identical in both summaries
    identical_artefacts_content = set(base) & set(head)

    # Retrieve those which filename are also identical
    untouched_artefacts = []
    for artefact_content in identical_artefacts_content:
        old_filepath = base[artefact_content]
        new_filepath = head[artefact_content]
        if old_filepath == new_filepath:
            untouched_artefacts.append(old_filepath)

    return untouched_artefacts


def list_renamed_files(
    base: ContentToFilepathMapping, head: ContentToFilepathMapping
) -> FilepathMapping:
    """List artefacts for renamed from base to head.

    This means their content has not changed, but their file path has.

    Args:
        base (ContentToFilepathMapping): Mapping of artefacts content to their
            filename in the base summary.
        head (ContentToFilepathMapping): Mapping of artefacts content to their
            filename in the head summary.

    Returns:
        FilepathMapping: Mapping of old to new file paths of artefacts which
            content hasn't changed between base and head.
    """
    # List contents identical in both summaries
    identical_artefacts_content = set(base) & set(head)

    # Retrieve those which filenames have changed
    renamed_artefacts = {}
    for artefact_content in identical_artefacts_content:
        old_filepath = base[artefact_content]
        new_filepath = head[artefact_content]
        if old_filepath != new_filepath:
            renamed_artefacts[old_filepath] = new_filepath

    return renamed_artefacts


def list_deleted_files(
    base: ContentToFilepathMapping, head: ContentToFilepathMapping
) -> FilepathCollection:
    """List deleted artefacts, i.e., those whose content is only found in base.

    Args:
        base (ContentToFilepathMapping): Mapping of artefacts content to their
            filename in the base summary.
        head (ContentToFilepathMapping): Mapping of artefacts content to their
            filename in the head summary.

    Returns:
        FilepathCollection: List of file paths of artefacts which are only
            found in base.
    """
    return [base[artefact_content] for artefact_content in set(base) - set(head)]


def list_added_files(
    base: ContentToFilepathMapping, head: ContentToFilepathMapping
) -> FilepathCollection:
    """List added artefacts, i.e., those whose content is only found in head.

    Args:
        base (ContentToFilepathMapping): Mapping of artefacts content to their
            filename in the base summary.
        head (ContentToFilepathMapping): Mapping of artefacts content to their
            filename in the head summary.

    Returns:
        FilepathCollection: List of file paths of artefacts which are only
            found in head.
    """
    return [head[artefact_content] for artefact_content in set(head) - set(base)]
