/*
 * ArrayExample.java
 * This program demonstrates the use of arrays by creating an array of integers
 * and printing each element to the console.
 */

public class ArrayExample {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5}; // An array of integers

        System.out.println("Array elements:");
        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]); // Print each element
        }
    }
}
