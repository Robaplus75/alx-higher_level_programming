#!/usr/bin/node
// prints all characters of a Star Wars

const request = require('request');
const film = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${film}`;
request(url, (error, response, body) => {
  if (!error) {
    const chars = JSON.parse(body).characters;
    chars.forEach((chara) => {
      request(chara, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
