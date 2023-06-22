#!/usr/bin/node

const fs = require('fs');

// Get the file paths from the command-line arguments
const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const destinationPath = process.argv[4];

// Read the contents of fileA
fs.readFile(fileAPath, 'utf8', (err, dataA) => {
  if (err) {
    console.error(`Error reading ${fileAPath}: ${err.message}`);
    process.exit(1);
  }

  // Read the contents of fileB
  fs.readFile(fileBPath, 'utf8', (err, dataB) => {
    if (err) {
      console.error(`Error reading ${fileBPath}: ${err.message}`);
      process.exit(1);
    }

    // Concatenate the contents of fileA and fileB
    const concatenatedData = dataA + dataB;

    // Write the concatenated data to the destination file
    fs.writeFile(destinationPath, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${destinationPath}: ${err.message}`);
        process.exit(1);
      }
    });
  });
});
