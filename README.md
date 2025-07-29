# MTech-Dissertation-Rpi-NAS
Building a Smart NAS System Using Raspberry Pi 4B with Bluetooth File Transfer and WhatsApp Alerts

#Objectives 
-NAS Implementation: Build a fully functional NAS on Raspberry Pi 4B with external storage and Samba/CIFS sharing, accessible to Windows/Linux/Android clients.

-Bluetooth File Transfer: Enable the Pi to receive files via Bluetooth OBEX (bluez/obexpushd), automating the Bluetooth file-upload service on boot.

-Alert Automation: Develop Python scripts to monitor system status (disk usage, connectivity) and send real-time WhatsApp alerts through Twilio API when thresholds/events occur.

-Web Dashboard : Create a Flask web interface hosted on the Pi to display system metrics (disk, CPU, memory, active users, recent uploads) in-browser over LAN.

-Security (CIA Triad): Design security for Confidentiality (user-authenticated Samba, storage encryption), Integrity (checksums, change-logging, backups) and Availability (RAID redundancy, auto-restart, health alerts).


