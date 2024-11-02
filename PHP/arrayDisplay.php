<?php
/*
 * arrayDisplay.php
 * This script creates an array of fruits and displays them in an HTML table.
 */

// Create an array of fruits
$fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"];

echo '<h1>Fruit List</h1>';
echo '<table border="1">
        <tr>
            <th>Index</th>
            <th>Fruit</th>
        </tr>';

// Loop through the array and display each fruit in a table row
foreach ($fruits as $index => $fruit) {
    echo '<tr>
            <td>' . $index . '</td>
            <td>' . $fruit . '</td>
          </tr>';
}

echo '</table>';
?>
