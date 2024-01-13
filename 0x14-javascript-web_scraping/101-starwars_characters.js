#!/usr/bin/node
const request = require('request');
if (process.argv.length !== 3) {
  console.error('Usage: node 101-starwars_characters.js <id>');
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

      const fetchCharacterData = async (characterUrl) => {
        return new Promise((resolve) => {
          request(
            characterUrl,
            (characterError, characterResponse, characterBody) => {
              if (characterError || characterResponse.statusCode !== 200) {
                resolve(null); // Resolve with null for error cases
              } else {
                const characterData = JSON.parse(characterBody);
                resolve(characterData.name);
              }
            }
          );
        });
      };
      Promise.all(resData.characters.map(fetchCharacterData))
        .then((characterNames) => {
          characterNames.forEach((name) => {
            if (name !== null) {
              console.log(name);
            } else {
              console.log('Error fetching character data');
            }
          });
        })
        .catch((error) => {
          console.error(error);
        });
    } catch (error) {
      console.error(error);
    }
  }
});
