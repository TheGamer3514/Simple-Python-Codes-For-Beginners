<?php
/*
 * formSubmit.php
 * This script displays a form that takes a user's name and displays a greeting message 
 * upon submission.
 */

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']); // Get the submitted name and sanitize it
    echo "Hello, " . $name . "! Welcome to our website.";
} else {
    // Display the form
    echo '<form method="POST" action="">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name" required>
            <input type="submit" value="Submit">
          </form>';
}
?>
