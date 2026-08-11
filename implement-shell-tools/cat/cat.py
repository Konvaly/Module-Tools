import argparse
import sys

parser = argparse.ArgumentParser(
    prog="cat",
    description="Concatenate files and print on the standard output",
)
parser.add_argument("-n", "--number", action="store_true",
                    help="Number all output lines")
parser.add_argument("-b", "--number-nonblank", action="store_true",
                    help="Number non-empty output lines, overrides -n")
parser.add_argument("files", nargs="+", help="The files to print")

args = parser.parse_args()

counter = 0
for path in args.files:
    with open(path, "r") as f:
        for line in f:
            if args.number_nonblank:
                if line.strip("\n") == "":
                    sys.stdout.write(line)
                else:
                    counter += 1
                    sys.stdout.write(f"{counter:6}\t{line}")
            elif args.number:
                counter += 1
                sys.stdout.write(f"{counter:6}\t{line}")
            else:
                sys.stdout.write(line)