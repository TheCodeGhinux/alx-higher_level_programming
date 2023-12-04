#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
const computed = list.map((num, i) => num * i);
console.log(computed);
