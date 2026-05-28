import argparse

parser = argparse.ArgumentParser(
    prog="wc",
    description="Count lines, words and characters in files",
)

parser.add_argument(
    "-l",
    action="store_true",
    help="Count lines only"
)

parser.add_argument(
    "-w",
    action="store_true",
    help="Count words only"
)

parser.add_argument(
    "-c",
    action="store_true",
    help="Count characters only",
)

parser.add_argument(
    "paths",
    nargs="+",
    help="The file(s) to count",
)

args = parser.parse_args()

total_lines = 0
total_words = 0
total_chars = 0

counts = []

for path in args.paths:
    with open(path, "r") as f:
            content = f.read()

            lines = len(content.splitlines())
            words = len(content.split())
            chars = len(content)

            total_lines += lines
            total_words += words
            total_chars += chars

            counts.append((lines, words, chars, path))  

width_lines = max(len(str(total_lines)) + 1, 2)
width_words = max(len(str(total_words)) + 1, 3)
width_chars = max(len(str(total_chars)) + 1, 4)

for lines, words, chars, path in counts:
      if args.l:
            print(f"{lines:>{width_lines}} {path}")
      elif args.w:
            print(f"{words:>{width_words}} {path}")
      elif args.c:
            print(f"{chars:>{width_chars}} {path}")
      else:
            print(f"{lines:>{width_lines}}{words:>{width_words}}{chars:>{width_chars}} {path}")

if len(args.paths) > 1:
     if args.l:
           print(f"{total_lines:>{width_lines}} total")   
     elif args.w:
           print(f"{total_words:>{width_words}} total") 
     elif args.c:
           print(f"{total_chars:>{width_chars}} total")         
     else:
           print(f"{total_lines:>{width_lines}}{total_words:>{width_words}}{total_chars:>{width_chars}} total")  
      
