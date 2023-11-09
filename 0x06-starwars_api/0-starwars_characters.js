#!/usr/bin/node
const req = require("request");
const API_URL = "https://swapi-api.hbtn.io/api";

// check the length of arguments
if (process.argv.length > 2) {
  req(`${API_URL}/films/${process.argv[2]}/`, (error, _, body) => {
    if (error) {
      console.log(error);
    }
    const charURL = JSON.parse(body).characters;
    //   map through the list of characters
    const charName = charURL.map(
      (url) =>
        new Promise((resolve, reject) => {
          req(url, (promiseErr, __, charactersReqBody) => {
            if (promiseErr) {
              reject(promiseErr);
            }
            resolve(JSON.parse(charactersReqBody).name);
          });
        })
    );

    Promise.all(charName)
      .then((names) => console.log(names.join("\n")))
      .catch((allErr) => console.log(allErr));
  });
}

