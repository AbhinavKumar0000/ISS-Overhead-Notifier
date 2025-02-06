# ISS-Overhead-Notifier

ISS Overhead Notifier is a Python-based project that sends an SMS alert when the International Space Station (ISS) is flying overhead and visible in the night sky. The project integrates real-time ISS location tracking, weather APIs, and Twilio for messaging notifications.

This solution is ideal for space enthusiasts who never want to miss the chance to spot the ISS when conditions are perfect.

🛠 Features
🛰 ISS Location Tracking: Monitors the real-time location of the ISS using an open API.
🌙 Night-Time Check: Ensures notifications are only sent when the sky is dark enough for visibility.
📲 SMS Notifications: Leverages Twilio API to send alerts directly to the user’s phone.
☁️ Cloud Deployment Ready: Can run on platforms like PythonAnywhere for continuous monitoring.
🚀 How It Works
Track ISS Location: Checks if the ISS is within a defined range of the user's location.
Night-Time Visibility: Verifies whether it’s dark at the user's coordinates using the sunrise-sunset API.
Send Alert: If both conditions are met, sends an SMS via Twilio:
"Look UP! 👆 The ISS 🛰🌙 is above you in the sky."



