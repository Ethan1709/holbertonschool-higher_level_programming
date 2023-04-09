#!/usr/bin/node

const x = process.argv[2];
if (parseInt(x, 10)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
