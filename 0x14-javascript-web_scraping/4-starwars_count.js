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
      // Parse the JSON response
      const data = JSON.parse(body);

      // Filter films where Wedge Antilles (character ID 18) is present
      const result = data.results.filter((film) =>
        film.characters.includes(
          'https://swapi-api.alx-tools.com/api/people/18/'
        )
      );

      // Display the number of movies
      // console.log(
      //   `Number of movies with Wedge Antilles: ${result.length}`
      // )
      console.log(result.length);
    } catch (error) {
      console.error(error);
    }
  }
});
