#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);

fs.writeFile(String(args[0]), String(args[1]), function (err) {
  if (err) {
    return console.log(err);
  }
});
