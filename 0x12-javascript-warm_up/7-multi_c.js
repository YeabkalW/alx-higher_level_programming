#!/usr/bin/node

const myTimes = parseInt(process.argv.slice(2)[0]);

if (isNaN(myTimes)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myTimes; i++) {
    console.log('C is fun');
  }
}
