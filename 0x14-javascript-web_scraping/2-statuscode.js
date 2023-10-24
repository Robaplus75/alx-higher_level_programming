#!/usr/bin/node
// For displaying the status code of a request

const args = process.argv;
let request = require('request');
request(args[2], function (err, res, body) {
  if (err) {
    console.log('error:', err);
  } else console.log('code:', res && res.statusCode);
});
