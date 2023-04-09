#!/usr/bin/node

const args = process.argv.slice(2).map(str => parseInt(str, 10));
const argslen = args.length;
if (argslen === 0 || argslen === 1) {
  console.log('0');
} else {
  for (let i = 0; i < argslen - 1; i++) {
    for (let j = 0; j < argslen - i - 1; j ++) {
        if (args[j] > args[j + 1]) {
            let x = args[j];
            args[j] = args[j + 1];
            args[j + 1] = x;
        }
    }
}
console.log(args[argslen - 2]);
}
