#!/usr/bin/node

function fact (x) {
  if (x == 0 ) {
    return 1;
  } else {
    return x * fact(x - 1);
  }
}
let number = parseInt(process.argv[2]);
if (number >= 0) {
  const r = fact(number);
  console.log(r);
} else {
  console.log('1')
}
