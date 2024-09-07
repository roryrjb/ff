#!/usr/bin/env python3

import argparse
import fnmatch
import os
import sys


def walktree(root, ignored_patterns):
    try:
        with os.scandir(root) as it:
            for entry in it:
                if entry.is_dir() and not entry.is_symlink():
                    if not path_ignored(entry, ignored_patterns):
                        for entry in walktree(entry.path, ignored_patterns):
                            yield entry
                elif entry.is_file():
                    yield entry
    except Exception:
        pass


def get_ignored_patterns(ignore_files):
    paths = []

    for path in [p for p in ignore_files if os.path.exists(p)]:
        with open(path, "r") as fh:
            paths.extend([line.strip() for line in fh.readlines()])

    return paths


def path_ignored(entry, ignored_patterns):
    for pattern in ignored_patterns:
        if pattern.find("*") > -1:
            if fnmatch.fnmatch(entry.path, pattern):
                return True

        # TODO: does this work for directories?
        if entry.name == pattern:
            return True

    return False


def grep(match, path):
    try:
        with open(path, "r") as fh:
            lineno = 0
            for line in fh.readlines():
                lineno += 1
                idx = line.find(match)
                if idx > -1:
                    line = line.rstrip("\n")
                    print(f"{path}:{lineno}:{idx + 1}:{line}")
    except UnicodeDecodeError:
        pass


def action(args, entry):
    if args.grep is not None:
        grep(args.grep, entry.path)
    else:
        print(entry.path)


def main(args):
    ignore_files = [
        os.path.join(os.path.expanduser("~"), ".ffignore"),
        os.path.join(os.getcwd(), ".ffignore"),
    ]

    if args.ignore_file:
        for path in args.ignore_file:
            ignore_files.append(os.path.expanduser(path))

    ignored_patterns = get_ignored_patterns(set(ignore_files))

    if args.exclude:
        ignored_patterns.extend(args.exclude)

    for entry in walktree(args.dir, ignored_patterns):
        if path_ignored(entry, ignored_patterns):
            continue

        if args.match:
            if args.exact:
                if entry.name == args.match:
                    action(args, entry)
            elif args.glob:
                if fnmatch.fnmatch(entry.name, args.match):
                    action(args, entry)
            elif entry.path.find(args.match) > -1:
                action(args, entry)
        else:
            action(args, entry)


def cli():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("match", nargs="?", default=None)
    argparser.add_argument(
        "--grep",
        metavar="STRING",
        help="search for GREP in filtered files",
        action="store",
        default=None,
    )
    argparser.add_argument("-g", "--glob", help="glob match", action="store_true")
    argparser.add_argument("--exact", help="exact match", action="store_true")
    argparser.add_argument(
        "-d",
        "--dir",
        metavar="PATH",
        help="search in a specific directory",
        action="store",
        default=".",
    )
    argparser.add_argument(
        "--exclude",
        metavar="GLOB",
        help="additional globs to exclude",
        action="append",
    )
    argparser.add_argument("--ignore-file", metavar="PATH", action="append")
    args = argparser.parse_args()

    try:
        main(args)
    except (KeyboardInterrupt, BrokenPipeError):
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}.", file=sys.stderr)
        sys.exit(1)