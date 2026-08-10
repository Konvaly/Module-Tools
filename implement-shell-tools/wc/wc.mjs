import process from "node:process";
import { promises as fs } from "node:fs";
import { parseArgs } from "node:util";

const { values, positionals } = parseArgs({
  options: {
    lines: { type: "boolean", short: "l", default: false },
    words: { type: "boolean", short: "w", default: false },
    bytes: { type: "boolean", short: "c", default: false },
  },
  allowPositionals: true,
});

const noFlags = !values.lines && !values.words && !values.bytes;
const showLines = noFlags || values.lines;
const showWords = noFlags || values.words;
const showBytes = noFlags || values.bytes;

if (positionals.length === 0) {
  console.error("Usage: node wc.mjs [-l] [-w] [-c] <path>...");
  process.exit(1);
}

function countLines(content) {
  let count = 0;
  for (const character of content) {
    if (character === "\n") {
      count++;
    }
  }
  return count;
}

function countWords(content) {
  return content.split(/\s+/).filter((word) => word !== "").length;
}

const results = [];
const totals = { lines: 0, words: 0, bytes: 0 };

for (const path of positionals) {
  let buffer;
  try {
    buffer = await fs.readFile(path);
  } catch {
    console.error(`wc: ${path}: No such file or directory`);
    process.exitCode = 1;
    continue;
  }

  const content = buffer.toString("utf-8");
  const counts = {
    lines: countLines(content),
    words: countWords(content),
    bytes: buffer.length,
    name: path,
  };

  results.push(counts);
  totals.lines += counts.lines;
  totals.words += counts.words;
  totals.bytes += counts.bytes;
}

if (results.length > 1) {
  results.push({ ...totals, name: "total" });
}

const selectedCounts = [showLines, showWords, showBytes].filter(Boolean).length;
const skipPadding = selectedCounts === 1 && results.length === 1;

let width = 1;
if (!skipPadding) {
  for (const result of results) {
    for (const key of ["lines", "words", "bytes"]) {
      width = Math.max(width, String(result[key]).length);
    }
  }
}

for (const result of results) {
  const columns = [];
  if (showLines) columns.push(String(result.lines).padStart(width));
  if (showWords) columns.push(String(result.words).padStart(width));
  if (showBytes) columns.push(String(result.bytes).padStart(width));
  console.log(`${columns.join(" ")} ${result.name}`);
}
