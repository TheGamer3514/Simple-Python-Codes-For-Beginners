/*
 * input_example.js
 * This script asks for the user's name and age, then displays a greeting in the console.
 */

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question("Enter your name: ", name => {
    readline.question("Enter your age: ", age => {
        console.log(`Hello, ${name}! You are ${age} years old.`);
        readline.close();
    });
});
