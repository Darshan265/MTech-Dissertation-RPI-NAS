   **SETTING UP SAMBA ON RPI **

I.OBJECTIVES - User(Windows, Linux, MacOS or Android) in the same LAN will be able to upload and download files via drag and drop method.

   ## Prerequisites
- Raspberry Pi 4B with Raspberry Pi OS installed
- Network connectivity (Ethernet or Wi-Fi)
- External USB storage device (e.g., 128GB USB stick or HDD)
- Basic knowledge of Linux command-line operations

II. MOUNT THE USB DRIVE 
- **Update System Packages**
  - ```
    sudo apt update && sudo apt full-upgrade -y
    ```
- **Verify USB Storage Device**
  ```
  lsblk
  ```
  ```
  fdisk -l
  ```
  - Identify your device (e.g., `/dev/sda1`)
- **Create Mount Directory**
  ```
  sudo mkdir -p /mnt/usb128GB/share
  ```
- **Mount USB Storage**
  ```
  sudo mount /dev/sda1 /mnt/usb128GB
  ```
  - Verify with:  
    ```
    df -h
    ```  
    ```
    mount | grep usb128GB
    ```
- **Set Ownership and Permissions**
  ```
  sudo chown -R pi:pi /mnt/usb128GB/share
  ```
  ```
  sudo chmod -R 770 /mnt/usb128GB/share
  ```
- **Persistent Mount with fstab**
  ```
  sudo nano /etc/fstab
  ```
  - Add entry:
    ```
    /dev/sda1   /mnt/usb128GB   auto   defaults,nofail   0   0
    ```
  - Apply changes:  
    ```
    sudo umount /mnt/usb128GB
    ```  
    ```
    sudo mount -a
    ```

II.INSTALLATION
       ```
       sudo apt install samba samba-common-bin -y
       ```

    
III. CONFIGURATION
- **Backup Default Samba Config**
  ```
  sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.bkup
  ```
- **Configure Samba Share**
  ```
  sudo nano /etc/samba/smb.conf
  ```
  - Append at the end:
    ```
    [nas]
    comment = Network Storage
    path = /mnt/usb128GB/share
    browseable = yes
    writable = yes
    valid users = pi
    create mask = 0660
    directory mask = 0770
    force user = pi
    force group = pi
    ```

- **Create and Enable Samba User**
  ```
  sudo smbpasswd -a pi
   ```
   ```
  sudo smbpasswd -e pi
   ```

- **Restart Samba Services**
   ```
  sudo systemctl restart smbd nmbd
   ```

- **Get Raspberry Pi IP**
  ```
  ifconfig
  ```
  - Note down the IP for client access.
    

IV. VERIFICATION
    - **Access NAS from Client Devices**
      - Go to File Explorer> Network.
      - Select Path
      - Windows:  
      ```
      \\<raspberry_pi_ip>\nas
      ```
      
      - Linux: 
      
      ```
      smb://<raspberry_pi_ip>/nas
      ```

  - Check Samba service status:  
    ```
    systemctl status smbd
    ```
  - Validate Samba configuration:  
    ```
    testparm
    ```
- List available shares:  
   ```
   smbclient -L //<raspberry_pi_ip> -U pi
   ```

V. TROUBLESHOOTING
    - **Mount Failure**
  - Check device:
    ```
    lsblk
    ```
  - Check filesystem type:
    ```
    sudo blkid
    ```
  - If needed, install support:  
    ```
    sudo apt install exfat-fuse exfat-utils -y
    ```

- **Permission Denied**
  ```
  ls -ld /mnt/usb128GB/share
  ```
  ```
  sudo chown -R pi:pi /mnt/usb128GB/share
  ```
  ```
  sudo chmod -R 770 /mnt/usb128GB/share
  ```

- **Samba Service Issues**
  ```
  journalctl -xe
  ```
  ```
  testparm
  ```

- **Windows Client Access**
  - Ensure SMB protocol enabled.
  - Use IP address:
    ```
    \\192.168.x.x\nas
    ```

- **Linux Client Access**
  - ```
    sudo apt install smbclient cifs-utils -y
    ```
  - Mount manually:  
    ```
    sudo mount -t cifs //<raspberry_pi_ip>/nas /mnt \
    -o username=pi,password=<your_password>,rw,uid=$(id -u),gid=$(id -g)
    ```

- **USB Drive Power Issues**
  - Use a powered USB hub if drive disconnects frequently.

## Notes
- Replace `/dev/sda1` with the correct device ID if different.
- Ensure proper power supply for external HDDs.
- This guide uses **0660/0770 permissions** for better security (not 0777).
- Always keep a backup of your original `smb.conf`.

---

## License
This guide is provided under the MIT License for educational and personal use.    
