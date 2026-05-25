import argparse

parser = argparse.ArgumentParser(
    prog="cat",
    description="Concatenate and print files",
)

parser.add_argument(
    "-n",
    action="store_true",
    help="Number all output lines"
)

parser.add_argument(
    "-b",
    action="store_true",
    help="Number non-blank output lines"
)

parser.add_argument(
    "paths",
    nargs="+",
    help="The file(s) to print",
)

args = parser.parse_args()

line_number = 1

for path in args.paths:
    with open (path, "r") as f:
        lines = f.readlines()

    for line in lines:
        is_blank = line.strip() == ""

        if args.b:
            if is_blank:
                print(line, end="")
            else:
                print(f"{line_number:>6}\t{line}", end="")
                line_number += 1
        elif args.n:
            print(f"{line_number:>6}\t{line}", end="")
            line_number += 1
        else:
            print(line, end="")