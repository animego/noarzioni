<?php

      $name = $_POST['name'];
      $visitor_email = $_Post['email'];
      $number = $_POST['number'];
      $home = $_POST['home'];
      $date = $_POST['date'];


      $mailheader = "From:".$name."<".$visitor_email.">\r\n";

      $recipient = "eytam20@gmail.com";


      $to = 'noarsocialistic@gmail.com';

      mail($to,$recipient,$number,$home,$date,$mailheader);

      header("Location: hiztarfut.html");

      echo'
<!DOCTYPE html>
<html lang="heb">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact form</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=Poppins&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Thank you for contacting me. I will get back to you as soon as possible!</h1>
        <p class="back">Go back to the <a href="index.html">homepage</a>.</p>
        
    </div>
</body>
</html>
';


?>
