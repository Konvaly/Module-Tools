import argparse
import os
import sys

parser = argparse.ArgumentParser(prog="ls", description="List directory contents")
parser.add_argument("-1", dest="one_per_line", action="store_true",
                    help="List one file per line")
parser.add_argument("-a", "--all", action="store_true",
                    help="Do not ignore entries starting with .")
parser.add_argument("paths", nargs="*", default=["."],
                    help="The files or directories to list")

args = parser.parse_args()


def entries(directory):
    names = os.listdir(directory)
    if args.all:
        names = names + [".", ".."]
    else:
        names = [name for name in names if not name.startswith(".")]
    return sorted(names)


files = []
directories = []
for path in args.paths:
    if os.path.isdir(path):
        directories.append(path)
    elif os.path.exists(path):
        files.append(path)
    else:
        print(f"ls: cannot access '{path}': No such file or directory",
              file=sys.stderr)

files.sort()
directories.sort()

show_headers = len(args.paths) > 1
printed_anything = False

for path in files:
    print(path)
    printed_anything = True

for directory in directories:
    if show_headers:
        if printed_anything:
            print()
        print(f"{directory}:")
    for name in entries(directory):
        print(name)
    printed_anything = True