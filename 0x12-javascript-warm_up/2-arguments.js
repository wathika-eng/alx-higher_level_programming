#!/usr/bin/node
/* Script that prints a message depending of the number of arguments passed
    * Output format: <number of arguments already printed>: <argument>
    * If no arguments are passed to the script, print No argument
 */

const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else if (args.length > 1) {
  console.log('Arguments found');
}
