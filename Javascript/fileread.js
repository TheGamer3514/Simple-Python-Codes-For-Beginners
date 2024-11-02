/*
 * fileread.js
 * This script opens a file and prints its contents to the console.
 */

const fs = require('fs');

// Reading from the file
fs.readFile('other/file.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading the file:', err);
        return;
    }
    console.log(data);
});
