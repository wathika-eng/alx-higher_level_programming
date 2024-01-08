#!/usr/bin/node
/* Script that prints the first argument passed to it
  * If no arguments are passed to the script, print “No argument”
  * You must use console.log(...) to print all output
  * You are not allowed to use var
 */

const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('No argument');
} else if (args.length >= 1) {
  console.log(args[0]);
}
