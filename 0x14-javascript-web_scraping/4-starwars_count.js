#!/usr/bin/node
// prints the number of movies where Wedge Antilles is present

const args = process.argv;
let reqURL = args[2];
let request = require('request');
request(reqURL, function (err, res, body) {
  if (err) {
    console.log('error:', err);
  } else {
    let jss = JSON.parse(body);
    let res = jss['results'];
    let c = 0;
    for (let i = 0; i < res.length; i++) {
      let chars = (res[i]['characters']);
      for (let j = 0; j < chars.length; j++) {
        let chec18 = chars[j].endsWith('18/');
        if (chec18) {
          c++;
        }
      }
    }
    console.log(c);
  }
});
