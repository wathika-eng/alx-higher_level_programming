#!/usr/bin/node
// Script that prints My number: <first argument converted in integer>

const myArgs = process.argv.slice(2);
if (isNaN(myArgs[0])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(myArgs[0]));
}
