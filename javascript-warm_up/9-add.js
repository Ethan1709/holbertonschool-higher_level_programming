#!/usr/bin/node

function add (a, b) {
  a = parseInt(process.argv[2], 10);
  b = parseInt(process.argv[3], 10);
  console.log(a + b);
}
add(process.argv[2], process.argv[3]);
