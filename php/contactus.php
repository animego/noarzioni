<?php

      $name = $_POST['name'];
      $visitor_email = $_Post['email'];
      $message = $_POST['message'];

      $email_from = 'eytam20@gmail.com';
      $email_subject = 'New Form Submission';
      $email_body = 'User Name:$name.\n'."
      User Email:$visitor_email.\n".
      "User Message:$message.\n";

      $to = 'noarsocialistic@gmail.com';
      $headers = "From: $email_from \r\n";
      mail($to,$email_subject,$email_body,$headers);
      header("Location: contactus.html");

?>