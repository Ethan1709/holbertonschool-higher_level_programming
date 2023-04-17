#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const api_url = String(process.argv[2]);
const file = String(process.argv[3]);

request.get(api_url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  fs.writeFile(file, body, (error) => {
    if (error) {
      console.error(error);
    }
  });
});
