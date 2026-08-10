import process from "node:process";
import { promises as fs } from "node:fs";
import { parseArgs } from "node:util";

const { values, positionals } = parseArgs({
  options: {
    one: { type: "boolean", short: "1", default: false },
    all: { type: "boolean", short: "a", default: false },
  },
  allowPositionals: true,
});

const showAll = values.all;
const paths = positionals.length > 0 ? positionals : ["."];

function stripPunctuation(name) {
  return name.replace(/[^\p{L}\p{N}]/gu, "");
}

function compareNames(a, b) {
  const result = stripPunctuation(a).localeCompare(stripPunctuation(b));
  return result !== 0 ? result : a.localeCompare(b);
}

const files = [];
const directories = [];

for (const path of paths) {
  try {
    const stats = await fs.stat(path);
    if (stats.isDirectory()) {
      directories.push(path);
    } else {
      files.push(path);
    }
  } catch {
    console.error(`ls: cannot access '${path}': No such file or directory`);
    process.exitCode = 2;
  }
}

files.sort(compareNames);
directories.sort(compareNames);

const needHeaders = directories.length > 1 || files.length > 0;
let printedSomething = false;

for (const file of files) {
  console.log(file);
  printedSomething = true;
}

for (const dir of directories) {
  let entries = await fs.readdir(dir);

  if (showAll) {
    entries = [".", "..", ...entries];
  } else {
    entries = entries.filter((entry) => !entry.startsWith("."));
  }
  entries.sort(compareNames);

  if (needHeaders) {
    if (printedSomething) {
      console.log("");
    }
    console.log(`${dir}:`);
  }

  for (const entry of entries) {
    console.log(entry);
  }
  printedSomething = true;
}
