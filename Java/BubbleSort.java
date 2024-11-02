/*
 * BubbleSort.java
 * This program sorts an array of integers using the Bubble Sort algorithm.
 */

import java.util.Arrays;

public class BubbleSort {
    public static void main(String[] args) {
        int[] numbers = {64, 34, 25, 12, 22, 11, 90};
        int n = numbers.length;

        System.out.println("Original array: " + Arrays.toString(numbers));

        // Bubble Sort Algorithm
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (numbers[j] > numbers[j + 1]) {
                    // Swap numbers[j] and numbers[j + 1]
                    int temp = numbers[j];
                    numbers[j] = numbers[j + 1];
                    numbers[j + 1] = temp;
                }
            }
        }

        System.out.println("Sorted array: " + Arrays.toString(numbers));
    }
}
