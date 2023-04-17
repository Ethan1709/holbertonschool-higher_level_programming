#!/usr/bin/node

const request = require('request');
let c = 1;
const dict = {};
let k = 0;
let t = 0;
api_url = String(process.argv[2]);

request({
  url: api_url,
  json: true
}, (err, response, body) => {
  if (err) {
    console.log('Error:', err);
  } for (const i in body) {
    k += 1;
    if (k % 20 === 0) {
      if (body[i].completed === true) {
        t += 1;
      }
      dict[c] = t;
      t = 0;
      c += 1;
    }
    if (body[i].userId === c) {
      if (body[i].completed === true) {
        t += 1;
      }
    }
    // console.log(body[i].completed)
  }
  console.log(dict);
  // console.log(body);
});

// body[i].userId = avoir l'userId
// je dois filtrer les true dans body[i[j]]
