# Artefacts Comparison

> `artefactscomparison` is a Python package to compare and report on two artefacts summaries.

An _artefact summary_ is a CSV listing files' paths and SHA512 sum. Assuming artefacts are saved under the `results/` directory, an _artefact summary_ is generated as follows:

```shell
$ find results/ -type f `# list files in the 'results/' directory…`\
    -exec sha512sum {} \; `# … and compute their SHA-512 sum`\
    | sed 's/  /,/' `# use comma — instead of double space — as separator`\
    | cat <(echo 'sha512,file_name') - `# add header to CSV`

sha512,file_name
<SHA512>,results/artefact_1
<SHA512>,results/path/to/artefact_2
```

The `artefactscomparison` package provides a CLI entry point that outputs a diff report on two artefacts summaries:

```diff
$ artefacts_comparison --base base_artefact_summary.csv --head head_artefact_summary.csv

@@ 3 file(s) added @@
+ path/to/new_file_1
+ path/to/new_file_2
+ path/to/new_file_3

@@ 1 file(s) deleted @@
- path/to/removed_file.csv

@@ 2 file(s) renamed @@
! path/to/to_rename_1 ￫ path/to/renamed_1
! path/to/to_rename_2 ￫ path/to/renamed_2

# 2 other file(s) remain unmodified
```

## User Quickstart

### Installation

You can install `artefactscomparison` from PyPI:

```shell
pip install artefactscomparison
```

### How to use

From the command line:

```shell
artefacts_comparison --head head_artefact_summary.csv --base base_artefact_summary.csv
```

where:

* `head_artefact_summary.csv` is the artefact summary of the branch you want to merge,
* `base_artefact_summary.csv` is the artefact summary of the branch your PR points to (i.e. `main`, `master`, etc.).

## Development Quickstart

This project adheres to [Semantic Versioning](https://semver.org/), and releases descriptions can be found in `CHANGELOG.md`.

### Use your own environment management preference

For `pyvenv`:

```shell
python -m venv .venv/
source .venv/bin/activate
```

### Install this package

```shell
git clone git@github.com:EBoisseauSierra/artefacts_comparison.git
cd artefacts_comparison
pip install --upgrade pip
pip install -e '.[dev,test]'
```

### Initialise pre-commit hooks

The [pre-commit hooks](https://pre-commit.com) defined in this repo ensure that code formating and linting is applied on any piece of code committed. This should enable a cleaner code base and less “formatting noise” in commits.

To install the hooks, simply run:

```shell
pre-commit install
```

### Contributing

1. Fork this repo (<https://github.com/EBoisseauSierra/artefacts_comparison/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Licence

Distributed under the MIT License. See `LICENSE` for more information.

## References

* Add comments on multi-line shell commands: https://stackoverflow.com/a/12797512/5433628
* Compute the SHA sum of all files in a directory: https://askubuntu.com/a/1091369
* Prefix the stdout: https://stackoverflow.com/a/33139133/5433628
