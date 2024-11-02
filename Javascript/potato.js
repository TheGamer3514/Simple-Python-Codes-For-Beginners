/*
 * potato.js
 * This script demonstrates file handling in Node.js by writing a sequence of strings 
 * to a file named 'temp.txt' and then reading and printing its contents to the console.
 */

const fs = require('fs');

// Writing to the file
fs.writeFileSync('temp.txt', '1 potato\n2 potato\n3 potato\n4\n5 potato\n6 potato\n7 potato\nMore!');

// Reading from the file
const data = fs.readFileSync('temp.txt', 'utf8');
console.log(data);
