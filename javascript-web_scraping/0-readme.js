#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);

fs.readFile(String(args), 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
