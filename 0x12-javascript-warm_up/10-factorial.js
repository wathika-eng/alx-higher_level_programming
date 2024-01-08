#!/usr/bin/node
const a = parseInt(process.argv[2]);
function factorial (a) {
  if (a === 0 || isNaN(a)) {
    return 1;
  }
  return a * factorial(a - 1);
}
console.log(factorial(a));
