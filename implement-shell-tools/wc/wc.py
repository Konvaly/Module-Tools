import argparse
import os

parser = argparse.ArgumentParser(prog="wc", description="Print newline, word and byte counts")
parser.add_argument("-l", "--lines", action="store_true", help="Print the newline counts")
parser.add_argument("-w", "--words", action="store_true", help="Print the word counts")
parser.add_argument("-c", "--bytes", action="store_true", help="Print the byte counts")
parser.add_argument("files", nargs="+", help="The files to count")

args = parser.parse_args()

show_all = not (args.lines or args.words or args.bytes)
show_lines = args.lines or show_all
show_words = args.words or show_all
show_bytes = args.bytes or show_all

rows = []
total = [0, 0, 0]

for path in args.files:
    with open(path, "rb") as f:
        data = f.read()
    counts = [data.count(b"\n"), len(data.split()), len(data)]
    for i in range(3):
        total[i] += counts[i]
    rows.append((counts, path))

if len(args.files) > 1:
    rows.append((total, "total"))
    width = len(str(sum(os.path.getsize(path) for path in args.files)))
else:
    width = 1


def selected(counts):
    chosen = []
    if show_lines:
        chosen.append(counts[0])
    if show_words:
        chosen.append(counts[1])
    if show_bytes:
        chosen.append(counts[2])
    return chosen


for counts, label in rows:
    columns = " ".join(f"{value:{width}}" for value in selected(counts))
    print(f"{columns} {label}")