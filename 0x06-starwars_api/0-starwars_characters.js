#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: ./<script> <film_id>');
  process.exit(1);
}

const filmId = process.argv[2];

request(`https://swapi-api.hbtn.io/api/films/${filmId}/`, function (err, res, body) {
  if (err) {
    console.error('Error:', err);
    return;
  }
  if (res.statusCode !== 200) {
    console.error('Error: Invalid response from API');
    return;
  }

  let actors;
  try {
    actors = JSON.parse(body).characters;
  } catch (e) {
    console.error('Error parsing JSON:', e);
    return;
  }

  exactOrder(actors, 0);
});

const exactOrder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, res, body) {
    if (err) {
      console.error('Error:', err);
      return;
    }
    if (res.statusCode !== 200) {
      console.error('Error: Invalid response from API');
      return;
    }

    let character;
    try {
      character = JSON.parse(body).name;
    } catch (e) {
      console.error('Error parsing JSON:', e);
      return;
    }

    console.log(character);
    exactOrder(actors, x + 1);
  });
};

