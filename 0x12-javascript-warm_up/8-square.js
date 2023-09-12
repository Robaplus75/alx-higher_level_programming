#!/usr/bin/node

const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let yax = 0;
    let myVar = '';

    while (yax < x) {
      myVar = myVar + 'X';
      yax++;
    }
    console.log(myVar);
  }
}
