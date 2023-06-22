#!/usr/bin/node

const mySize = parseInt(process.argv.slice(2)[0]);

if (isNaN(mySize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < mySize; i++) {
    for (let j = 0; j < mySize; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
