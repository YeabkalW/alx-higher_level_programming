#!/usr/bin/node

const { dict } = require('./101-data');

const sortedDict = {};

for (const userId in dict) {
  const occurrence = dict[userId];
  if (occurrence in sortedDict) {
    sortedDict[occurrence].push(userId);
  } else {
    sortedDict[occurrence] = [userId];
  }
}

console.log(sortedDict);
