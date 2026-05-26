import argparse
import os

parser = argparse.ArgumentParser(
    prog="ls",
    description="List directory content",
)

parser.add_argument(
    "-1",
    action="store_true",
    dest="one",
    help="List one file per line",
)

parser.add_argument(
    "-a",
    action="store_true",
    help="Do not ignore entries starting with .",
)

parser.add_argument(
    "path",
    nargs="?",
    default=".",
    help="The directory to list",
)

args = parser.parse_args()

items = os.listdir(args.path)

if args.a:
    items = [".", ".."] + items
else:
    items = [item for item in items if not item.startswith(".")]

items = sorted(items, key=lambda item: item.lstrip(".").lower())

for item in items:
    print(item)