/*
 * Factorial.java
 * This program calculates the factorial of a number using a for loop.
 */

public class Factorial {
    public static void main(String[] args) {
        int number = 5; // Change this number to compute a different factorial
        int factorial = 1;

        for (int i = 1; i <= number; i++) {
            factorial *= i; // factorial = factorial * i
        }

        System.out.println("Factorial of " + number + " is " + factorial);
    }
}
