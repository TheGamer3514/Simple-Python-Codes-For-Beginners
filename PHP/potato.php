<?php
/*
 * potato.php
 * This script generates a sequence of strings and displays them in the browser.
 */

$potatoList = [];

// Generate potato entries
for ($n = 1; $n <= 3; $n++) {
    $potatoList[] = $n . " potato";
}
$potatoList[] = "4";
for ($n = 5; $n <= 7; $n++) {
    $potatoList[] = $n . " potato";
}
$potatoList[] = "More!";

// Echo the results in the HTML
foreach ($potatoList as $item) {
    echo $item . "<br>";
}
?>
