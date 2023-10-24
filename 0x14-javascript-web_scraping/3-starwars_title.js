#!/usr/bin/node
// prints the title of star wars

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, res, body) {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
