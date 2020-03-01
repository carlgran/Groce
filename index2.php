<head></head>
<body class="page_bg">
Hello, today is <?php echo date('l, F jS, Y'); ?>.
<?php
$servername = "localhost";
$username = "root";
$password = " "; 

// Create connection
$conn = new mysqli($servername, $username);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
echo "Connected successfully";
?>

</body>
</html>