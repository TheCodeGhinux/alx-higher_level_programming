#!/usr/bin/node
const MainSquare = require('./5-square.js');
class Square extends MainSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
