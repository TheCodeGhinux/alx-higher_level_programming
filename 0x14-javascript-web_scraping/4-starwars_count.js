#!/usr/bin/node
const request = require('request');
if (process.argv.length !== 3) {
  console.error('Usage: node 4-starwars_count.js <url>');
  process.exit(1);
}

const apiUrl = process.argv[2];
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const data = JSON.parse(body).results;
      const result = data.filter((film) =>
        film.characters.some((character) => character.endsWith('/18/'))
      );
      console.log(result.length);
    } catch (error) {
      console.error(error);
    }
  }
});
