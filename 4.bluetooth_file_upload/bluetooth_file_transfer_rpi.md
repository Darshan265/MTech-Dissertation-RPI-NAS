# 📂 Bluetooth File Transfer on Raspberry Pi NAS

This guide explains how to set up your Raspberry Pi as a **Bluetooth
file receiver** using the OBEX Object Push (OPP) profile.\
Once configured, you can **send files from your phone or laptop via
Bluetooth** to the Pi, and they will automatically be saved into:

/mnt/usb128GB/share

yaml Copy code

That folder is already used by Samba and your Flask NAS dashboard, so
new files will appear there immediately.

------------------------------------------------------------------------

## ⚙️ Setup on Raspberry Pi

### 1. Install required packages

\`\`\`bash sudo apt-get update sudo apt-get install -y bluez bluez-obexd
dbus-user-session 2. Prepare the storage folder bash Copy code sudo
mkdir -p /mnt/usb128GB/share sudo chown -R pi:pi /mnt/usb128GB/share
sudo chmod -R 770 /mnt/usb128GB/share 3. Enable Bluetooth and pair
devices Start the Bluetooth tool:

bash Copy code sudo bluetoothctl Inside the prompt:

text Copy code power on agent on default-agent discoverable on pairable
on scan on When your phone/laptop appears, pair and trust it (replace
MAC with your device's address):

text Copy code pair XX:XX:XX:XX:XX:XX trust XX:XX:XX:XX:XX:XX quit 4.
Manual test (one-off run) Run the OBEX server directly:

bash Copy code /usr/libexec/bluetooth/obexd --noplugin=pcap
--auto-accept --root=/mnt/usb128GB/share Leave this running. Try sending
a file from your phone (see next section). Check the folder:

bash Copy code ls -lh /mnt/usb128GB/share 5. Auto-start at boot Create a
user service for Pi:

bash Copy code mkdir -p \~/.config/systemd/user nano
\~/.config/systemd/user/obex.service Paste:

ini Copy code \[Unit\] Description=Bluetooth OBEX File Server for NAS
After=dbus-user-session.service Wants=dbus-user-session.service

\[Service\] ExecStart=/usr/libexec/bluetooth/obexd --noplugin=pcap
--auto-accept --root=/mnt/usb128GB/share Restart=on-failure

\[Install\] WantedBy=default.target Enable it:

bash Copy code systemctl --user daemon-reload systemctl --user enable
--now obex.service sudo loginctl enable-linger pi Now it will auto-run
at boot.

📱 From the Sender's Device (User's Perspective) Here's what sending
files looks like for people using your NAS:

Android Phone Open the file (photo, video, document).

Tap Share → Bluetooth.

Choose raspberrypi (or the Pi's Bluetooth name).

Wait until the transfer completes.

The file is now in the Pi's NAS folder.

iPhone (limited) iOS doesn't support generic Bluetooth file transfer
(only AirDrop).

Use Samba or Flask dashboard for iPhone uploads instead.

Windows Laptop Right-click the file → Send to → Bluetooth device.

Select raspberrypi.

Confirm the transfer.

File arrives in the NAS folder.

macOS In Finder: Go → Send File to Device....

Pick raspberrypi.

Confirm transfer.

File lands in the NAS folder.

Linux Laptop Use your desktop's Bluetooth menu → Send File.

Choose raspberrypi.

Confirm on the laptop.

File appears in the NAS folder.

✅ Verifying Transfers On the Pi:

bash Copy code ls -lh /mnt/usb128GB/share Or, simply refresh the Flask
NAS dashboard in your browser --- the new file will be listed.

🔧 Troubleshooting ❌ "transfer forbidden by target device" Cause: The
Pi has not trusted your device, or obexd isn't running with
--auto-accept.

Fix: In bluetoothctl, run:

text Copy code trust XX:XX:XX:XX:XX:XX connect XX:XX:XX:XX:XX:XX Then
restart the OBEX daemon:

bash Copy code systemctl --user restart obex.service ❌ "Name already in
use" Cause: Another obexd instance is already running.

Fix: Stop the default one and use your custom service:

bash Copy code systemctl --user stop obex.service systemctl --user
disable obex.service pkill obexd Then restart your NAS service.

❌ "Couldn't connect to DBus session bus" Cause: Running bt-obex or
obexd with sudo (root) but no D-Bus session.

Fix: Run as the pi user (no sudo), or use the systemd user service.

❌ Files don't appear in /mnt/usb128GB/share Check the OBEX service
logs:

bash Copy code journalctl --user -u obex.service -f Ensure the folder
exists and is writable by pi:

bash Copy code sudo chown -R pi:pi /mnt/usb128GB/share sudo chmod -R 770
/mnt/usb128GB/share 🔒 Security Notes Only paired + trusted devices can
send files.

--auto-accept means any trusted device can drop files without asking.
Use only with devices you control.

To disable auto-accept, remove --auto-accept and start obexd manually
when needed.

🎉 Summary Tech user: manages setup with systemctl and logs.

End user (phone/laptop): just uses the normal Send via Bluetooth option,
chooses Raspberry Pi, and files appear in the NAS folder automatically.
