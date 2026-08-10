import process from "node:process";
import { promises as fs } from "node:fs";
import { parseArgs } from "node:util";

const { values, positionals } = parseArgs({
  options: {
    number: { type: "boolean", short: "n", default: false },
    "number-nonblank": { type: "boolean", short: "b", default: false },
  },
  allowPositionals: true,
});

const numberAll = values.number;
const numberNonBlank = values["number-nonblank"];

if (positionals.length === 0) {
  console.error("Usage: node cat.js [-n] [-b] <path>...");
  process.exit(1);
}

let lineNumber = 1;

for (const path of positionals) {
  let content;
  try {
    content = await fs.readFile(path, "utf-8");
  } catch {
    console.error(`cat: ${path}: No such file or directory`);
    process.exitCode = 1;
    continue;
  }

  if (!numberAll && !numberNonBlank) {
    process.stdout.write(content);
    continue;
  }

  const lines = content.split("\n");
  const endsWithNewline = lines[lines.length - 1] === "";
  if (endsWithNewline) {
    lines.pop();
  }

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const isLastLine = i === lines.length - 1;
    const lineEnding = !isLastLine || endsWithNewline ? "\n" : "";

    if (numberNonBlank && line === "") {
      process.stdout.write(lineEnding);
    } else {
      process.stdout.write(
        `${String(lineNumber).padStart(6)}\t${line}${lineEnding}`,
      );
      lineNumber++;
    }
  }
}
