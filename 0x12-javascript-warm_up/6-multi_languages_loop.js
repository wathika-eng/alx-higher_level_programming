#!/usr/bin/node
// Script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

const dict = ['C is fun', 'Python is cool', 'Javascript is amazing'];
for (const i in dict) {
  console.log(dict[i]);
}
