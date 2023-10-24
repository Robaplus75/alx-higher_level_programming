#!/usr/bin/node
// script that reads from files

const filesystem = require('fs');
filesystem.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
