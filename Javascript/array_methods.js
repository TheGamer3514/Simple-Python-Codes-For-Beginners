/*
 * array_methods.js
 * This script demonstrates array methods like map and filter.
 */

let numbers = [1, 2, 3, 4, 5];
let doubled = numbers.map(num => num * 2);
let evenNumbers = numbers.filter(num => num % 2 === 0);
console.log("Doubled:", doubled);
console.log("Even Numbers:", evenNumbers);
