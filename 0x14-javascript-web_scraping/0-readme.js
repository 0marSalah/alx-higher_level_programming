#!/usr/bin/node

const fs = require('fs');

const filename = process.argv[2];

try {
  const data = fs.readFileSync(filename, 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}
