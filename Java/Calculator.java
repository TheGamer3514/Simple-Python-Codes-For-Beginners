/*
 * Calculator.java
 * This program performs basic arithmetic operations based on user input.
 */

import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first number: ");
        double num1 = scanner.nextDouble();

        System.out.print("Enter second number: ");
        double num2 = scanner.nextDouble();

        System.out.println("Select operation: +, -, *, /");
        char operation = scanner.next().charAt(0);
        double result;

        switch (operation) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                result = num1 / num2;
                break;
            default:
                System.out.println("Invalid operation");
                return;
        }
        System.out.println("Result: " + result);
        scanner.close();
    }
}
