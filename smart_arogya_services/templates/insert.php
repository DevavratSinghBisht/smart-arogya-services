<?php
session_start();
header('location:Register.php');
$con = mysqli_connect('localhost','root','');
mysqli_select_db($con,'arogyaservicesdatabase');
$name = $_POST['Name'];
$username  = $_POST['UserName'];
$phone = $_POST['Phone'];
$email = $_POST['Email'];
$gender = $_POST['Gender'];
$password = $_POST['Password'];
$s = "select * from userinfo where UserName='$username'";

$result = mysqli_query($con, $s);
$num = mysqli_num_rows($result);
if($num == 1){
	echo "Username already taken";
}else {
	$reg = "insert into userinfo(Name,UserName,Phone,Email,Gender,Password) values ('$name','$username','$phone','$email','$gender','$password')";
	mysqli_query($con,$reg);
	echo "Registration Successful";
}


?>