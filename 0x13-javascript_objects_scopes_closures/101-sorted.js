#!/usr/bin/node
const dict = require('./101-data.js').dict;
const occurrences = {};
for (const ids in dict) {
  if (occurrences[dict[ids]] === undefined) {
    occurrences[dict[ids]] = [ids];
  } else {
    occurrences[dict[ids]].push(ids);
  }
}
console.log(occurrences);
