#!/usr/bin/node
// Script that prints 3 lines.
// The first line: “C is fun”, the second line: “Python is cool” and the third line: “Javascript is amazing”

const args = process.argv.slice(2);
if (args.length === 0 || isNaN(args[0])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < args[0]; i++) {
    console.log('C is fun');
  }
}
