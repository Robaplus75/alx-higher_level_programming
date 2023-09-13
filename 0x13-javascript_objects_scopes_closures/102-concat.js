#!/usr/bin/node
/*
 * alx javascript task 102
 */
const fs = require('fs');

const fileB = process.argv[3];
const fileA = process.argv[2];
const fileC = process.argv[4];

if (
  fs.existsSync(fileA) &&
fs.statSync(fileA).isFile &&
fs.existsSync(fileB) &&
fs.statSync(fileB).isFile &&
fileC !== undefined
) {
  const fileBContent = fs.readFileSync(fileB);
  const fileAcontent = fs.readFileSync(fileA);
  const stream = fs.createWriteStream(fileC);

  stream.write(fileAContent);
  stream.write(fileBContent);
  stream.end();
}
