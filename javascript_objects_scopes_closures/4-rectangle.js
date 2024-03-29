#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h <= 0 || w <= 0 || h == null || w == null) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const x = this.height;
    this.height = this.width;
    this.width = x;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
