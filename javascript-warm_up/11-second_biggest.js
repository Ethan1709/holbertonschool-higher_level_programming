#!/usr/bin/node

const args = process.argv.slice(2).map(str => parseInt(str, 10));
const args_len = args.length;
if (args_len === 0 || args_len === 1) {
  console.log('0');
} else {
  console.log(args);
  for (let i = 0; i < args_len - 1; i++) {
    for (let j = 0; j < args_len - i - 1; j ++) {
        if (args[j] > args[j + 1]) {
            let x = args[j];
            args[j] = args[j + 1];
            args[j + 1] = x;
            console.log(args);
        }
    }
}
console.log([args_len - 2]);
}
