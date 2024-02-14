#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return this.Object;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    if (this.width === 0 || this.height === 0) {
      pass;
    } else {
      const row = 'X'.repeat(this.width);
      for (i = 0; i < this.height; i++) {
        console.log(row);
      }
    }
  }
}

module.exports = Rectangle;
