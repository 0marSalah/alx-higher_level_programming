#!/usr/bin/node

const fs = require('fs');

const filename = process.argv[2];
const content = process.argv[3] + "\n";

try {
	fs.writeFileSync(filename, content, { encoding: "utf8" });
} catch (err) {
	console.error(err);
}
