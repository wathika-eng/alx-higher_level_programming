#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request.get(url, (error, response, body) => {
  if (error) {
    console.error;
  } else {
    const movie = JSON.parse(body);
    const Title = movie.title;
    console.log(`${Title}`);
  }
});
