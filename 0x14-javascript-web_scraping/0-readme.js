#!/usr/bin/node

const fs = require('fs');
file = process.argv[2];
fs.readFile(file, 'utf-8', (err, jsonString) => {
  if (err) {
    console.log(err);
  } else {
    console.log(jsonString);
  }
});
