#!/usr/bin/node

const request = require('request');
let c = 1;
const dict = {};
let k = 0;
let o = 1;
let t = 0;
const apiurl = String(process.argv[2]);

request({
  url: apiurl,
  json: true
}, (err, response, body) => {
  if (err) {
    console.log('Error:', err);
  } for (const i in body) {
    k = body[i].userId;
    if (k !== o && t !== 0) {
      dict[c] = t;
      t = 0;
      c += 1;
      o = k;
    }
    if (k === c) {
      if (body[i].completed === true) {
        t += 1;
      }
    }
  }
  if (t !== 0) {
    dict[c] = t;
  }
  console.log(dict);
});
