"""This module defines the CLI interface of the package."""

import click

from .csv_parser import get_content_to_filepath_mapping
from .report import Report


@click.command()
@click.option(
    "-b",
    "--base",
    required=True,
    help="Path to base's artefacts summary.",
    type=click.Path(exists=True),
)
@click.option(
    "-h",
    "--head",
    required=True,
    help="Path to head's artefacts summary.",
    type=click.Path(exists=True),
)
def artefacts_comparison(base, head):
    """Entry point of the program.

    The main function executes on commands:
    `python -m artefactscomparison` and `$ artefactscomparison `.
    This is your program's entry point.
    """
    base = get_content_to_filepath_mapping(base)
    head = get_content_to_filepath_mapping(head)

    report = Report(base=base, head=head).generate()

    print(report.to_str())
