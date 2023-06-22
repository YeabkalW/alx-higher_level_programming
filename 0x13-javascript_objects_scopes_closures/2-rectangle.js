#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      // creating new empty object
      return;
    }

    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
