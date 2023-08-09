#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const Url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(Url, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
    return;
  }

  const filmData = JSON.parse(body);
  const charactersUrls = filmData.characters;

  charactersUrls.forEach(characterUrl => {
    request(characterUrl, (characterError, characterResponse, characterBody) => {
      if (characterError) {
        console.error(characterError);
        return;
      }

      if (characterResponse.statusCode !== 200) {
        console.error(`Request failed with status code ${characterResponse.statusCode}`);
        return;
      }

      const characterData = JSON.parse(characterBody);
      console.log(characterData.name);
    });
  });
});

