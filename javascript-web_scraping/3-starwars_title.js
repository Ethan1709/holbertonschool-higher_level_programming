#!/usr/bin/node

const request = require('request');
id = process.argv[2];

request({
  url: `https://swapi-api.hbtn.io/api/films/${id}`,
  json: true
}, (err, response, body) => {
  console.log(body.title);
});
