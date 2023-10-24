#!/usr/bin/node
// Gets the contents of a webpage and store it

const fs = require('fs');
const request = require('request');

request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
