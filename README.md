# ff

## About

`ff` is a simple file "filter" that can be used as a cross-platform file finder.

## Installation

`ff` is a standard `setup.py` Python project, you can install by cloning the repo, or downloading the zip that Github provides and running `python setup.py ...` or using the Makefile.
For Windows I release a standalone exe with each release.

## Usage

Do `ff -h` for options, but basically you can use simple string matching, globs and also grep for strings in the "filtered file set".
One of the benefits `ff` has over let's say `find(1)` on Unix, is that you can add a bunch of glob excludes to a `.ffignore` file in the same directory or
the user global `~/.ffignore` / `%USERPROFILE\.ffignore` file.

```
usage: ff [-h] [--grep STRING] [-g] [--exact] [-d PATH] [--exclude GLOB] [--ignore-file PATH] [match]

positional arguments:
  match

options:
  -h, --help           show this help message and exit
  --grep STRING        search for GREP in filtered files
  -g, --glob           glob match
  --exact              exact match
  -d PATH, --dir PATH  search in a specific directory
  --exclude GLOB       additional globs to exclude
  --ignore-file PATH
```

## Quirks

This was original written on Linux with a planned vim quickfix integration, but I no longer use this setup, so there may be some baked in assumptions in places. Pull requests are welcome.
