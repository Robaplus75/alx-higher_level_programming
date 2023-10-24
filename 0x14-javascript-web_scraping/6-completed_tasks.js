#!/usr/bin/node
// computes the number of tasks completed

const args = process.argv;
let rURL = args[2];
let request = require('request');
request(rURL, function (err, res, body) {
  if (err) {
    console.log('error:', err);
  } else {
    let todo = JSON.parse(body);
    let d = {};
    for (let i = 0; i < todo.length; i++) {
      let status = (todo[i]['completed']);
      let key = todo[i]['userId'].toString();
      if (status) {
        if (d[key]) {
          d[key]++;
        } else {
          d[key] = 1;
        }
      }
    }
    console.log(d);
  }
});
