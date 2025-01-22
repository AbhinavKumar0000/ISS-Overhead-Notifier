# ISS-Overhead-Notifier

ISS Overhead Notifier
A Python script that checks if the International Space Station (ISS) is currently passing over a specified location and whether it is nighttime. If both conditions are met, the script sends an email notification to alert the user to look up at the sky.

Features:
Uses the open-notify API to track the ISS position.
Determines local sunrise and sunset times via the sunrise-sunset API.
Sends email notifications when the ISS is visible overhead at night.
Runs continuously, checking conditions every 60 seconds.

Technologies Used:
-Python
-requests for API calls
-smtplib for email notifications
-datetime for time handling

Setup Instructions:
-Update the script with your latitude and longitude.
-Enter your email credentials for notifications.
-Run the script and receive alerts when the ISS is visible.
