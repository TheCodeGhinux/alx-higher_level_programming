#!/usr/bin/node
const request = require('request');
const fs = require('fs');
if (process.argv.length !== 3) {
  console.error('Usage: node 6-completed_tasks.js <id>');
  process.exit(1);
}

const id = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${id}/`;
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const resData = JSON.parse(body);

      // console.log(`${resData.title}`)
      resData.characters.forEach((characterUrl) => {
        request(
          characterUrl,
          (characterError, characterRes, characterBody) => {
            if (characterError) {
              console.error(characterError);
            } else if (characterRes.statusCode !== 200) {
              console.error(
                `Error: ${characterRes.statusCode} - ${characterBody}`
              );
            } else {
              // Parse the character JSON response
              const charData = JSON.parse(characterBody);
              console.log(charData.name);
            }
          }
        );
      });
    } catch (error) {
      console.error(error);
    }
  }
});
