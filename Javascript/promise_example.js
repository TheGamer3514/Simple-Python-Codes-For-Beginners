/*
 * promise_example.js
 * This script demonstrates a basic Promise in JavaScript.
 */

let myPromise = new Promise((resolve, reject) => {
    let success = true;
    if (success) {
        resolve("Promise fulfilled!");
    } else {
        reject("Promise rejected.");
    }
});

myPromise
    .then(result => console.log(result))
    .catch(error => console.log(error));
