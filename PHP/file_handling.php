
<?php
// file_handling.php
// Writes a line of text to a file.

$file = fopen("output.txt", "w");
fwrite($file, "This is a file write example!");
fclose($file);
echo "Text written to output.txt";
?>
