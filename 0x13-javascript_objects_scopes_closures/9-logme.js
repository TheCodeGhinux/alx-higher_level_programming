#!/usr/bin/node
let printedNum = 0;
exports.logMe = function (item) {
  console.log(`${printedNum++}: ${item}`);
};
