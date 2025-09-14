# Flask-based NAS Dashboard on Raspberry Pi 4B – Build Guide
- This document explains step by step how to set up a **NAS dashboard** on a Raspberry Pi 4B using Flask.  
- The dashboard lets you upload, download, and manage files via a browser.  
- We also cover virtual environments and local network access.

## 1. Prepare the flask Setup

1. Connect your USB drive (e.g., 128 GB) to the Pi.  
 Find it:
   ```
   lsblk -f
   ```
2. Create mount points:
```
sudo mkdir -p /mnt/usb128GB/share   
```
3. Mount the drive:
```
sudo mount /dev/sda1 /mnt/usb128GB
sudo chmod 777 /mnt/usb128GB/share
```

4. Add to /etc/fstab:
- Determine UUID of USB Drive
```
  sudo blkid
  ```
- Open file
```
sudo nano /etc/fstab
```
- Add the following line at the end:
```
UUID=<UUID_of_usb_drive>  /mnt/usb128GB  vfat  defaults,uid=1000,gid=1000,umask=002,nofail  0 0
```
NOTE: replace <UUID_of_usb_drive> with UUID
e.g. UUID=669A-558B  /mnt/usb128GB  vfat  defaults,uid=1000,gid=1000,umask=002,nofail  0 0

4. Apply Changes
- Test without reboot:
```
sudo mount -a
```
- If no errors, check:
```
ls -lh /mnt/usb128GB
```

6. Verify on Reboot
- Reboot the Pi:
```
sudo reboot
```
- Then confirm the drive auto-mounts:
```
df -h | grep usb128GB
```
NOTE: 
- If your drive is formatted as ext4, use:
```
UUID=<your-uuid> /mnt/usb128GB ext4 defaults,noatime 0 0
```
- For FAT32/exFAT (vfat), use the uid/gid/umask options as shown above.
- To change ownership later:
```
sudo chown -R pi:pi /mnt/usb128GB
```

# Step 2: Install System Packages
1. Update and install Python 3 and pip on the Pi:
```
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install -y python3 python3-pip
```
2. Use a Python virtual environment (venv)
- To isolate this project’s Python dependencies (so they don’t affect the system or other projects)
```
python3 -m venv venv
```
- Activate it:
```
source /home/pi/nas_dashboard/venv/bin/activate
```
- Install Flask and Flask-Login (for authentication) inside the venv:
```
pip install flask flask-login
```
NOTE: When finished working on the project, deactivate the venv:
```
deactivate
```
3. Flask Application Code
- Create a directory "~/nas_dashboard/" and go inside it
```
mkdir nas_dashboard
```
```
cd /home/pi/nas_dashboard
```
- Create Application code
```
nano app.py
```
refer: app.py in present repository.

4. HTML Template
- Project Structure:
```
/home/pi/nas_dashboard/
├── app.py
├── venv/
└── templates/
    ├── login.html
    └── dashboard.html
```
- Create login.html  and dashboard.html in directory named "templates"
refer:present github repo

5. Run Flask Application:
- Note: run inside virtual virtual environment.
```
python app.py
```
6. Access in Browser
- Find Pi’s IP:
```
hostname -I
```
- Access locally:
```
http://<raspberry-pi-ip>:5000
```
- Or by hostname (if mDNS is working):
```
http://raspberrypi.local:5000
```
- Enter set login

  7. Verify working
- Check login, list of files, upload, download 
     refer: https://drive.google.com/file/d/1uAlnTGP1_5xUEHyBV0-FzBLQUw5fcXnR/view?usp=drive_link 
