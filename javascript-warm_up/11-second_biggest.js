#!/usr/bin/node

const args = process.argv.slice(2);
args_len = args.length;
if (args_len === 0 || args_len === 1) {
  console.log('0');
} else {
  for (let i = 0; i < args_len; i++) {
    if (args[i] > args[i + 1]) {
        let x = args[i];
        args[i] = args[i + 1];
        args[i + 1] = x;
    } if (args[i + 1] == null) {
        console.log(args[i - 1]);
    }
}
}