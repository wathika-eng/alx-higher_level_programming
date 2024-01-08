#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of arguments.

const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
}
const secondBiggest = args.sort((a, b) => b - a)[1];
console.log(secondBiggest);
