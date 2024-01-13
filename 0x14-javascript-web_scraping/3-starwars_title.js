#!/usr/bin/node
const request = require('request');
if (process.argv.length !== 3) {
  console.error('Usage: node 3-starwars_title.js <number>');
  process.exit(1);
}

const id = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${id}`;
request.get(apiUrl, (error, response, body) => {
  const resData = JSON.parse(body);
  if (error) {
    console.error(error);
  } else {
    console.log(resData.title);
  }
});
