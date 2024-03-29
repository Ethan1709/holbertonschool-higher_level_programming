#!/usr/bin/node

const request = require('request');
let count = 0;
const url = String(process.argv[2]);

request({
  url: url,
  json: true
}, (err, response, body) => {
  if (err) {
    console.log('Error:', err);
  } for (const i in body.results) {
    for (const j of body.results[i].characters) {
      if (j.match('18')) {
        count += 1;
      }
    }
  }
  console.log(count);
}
);
