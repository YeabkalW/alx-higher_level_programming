#!/usr/bin/node

const myNum = parseInt(process.argv.slice(2)[0]);

if (isNaN(myNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myNum);
}
