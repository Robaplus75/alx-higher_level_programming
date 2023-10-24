#!/usr/bin/node
// script for writing to files

const fs = require('fs');
const file = process.argv[2];
const text = process.argv[3];

fs.writeFile(file, text, (err) => {
  if (err) {
    console.log(err);
  }
}
);
