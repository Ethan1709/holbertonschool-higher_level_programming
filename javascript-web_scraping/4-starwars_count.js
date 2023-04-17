#!/usr/bin/node

const request = require('request');
let count = 0;

request({
  url: 'https://swapi-api.hbtn.io/api/films/',
  json: true
}, (err, response, body) => {
  if (err) {
    console.log('Error:', err);
  } for (const i in body.results) {
    for (const j of body.results[i].characters) {
      if (j == 'https://swapi-api.hbtn.io/api/people/18/') {
        count += 1;
      }
    }
  }
  console.log(count);
}
);
