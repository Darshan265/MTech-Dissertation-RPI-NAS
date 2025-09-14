# Prerequisite Setup
## I.Steps to Flash Raspberry Pi OS and Enable SSH
### Requirements
  -A computer (Windows, macOS, or Linux)
  -An SD card (8GB minimum recommended)
  -An SD card reader (if not built-in to your computer)
  -Raspberry Pi Imager software


1. Download and Install Raspberry Pi Imager
   -Go to the [Raspberry Pi Imager download page](https://www.raspberrypi.com/software/).
   -Download the appropriate version for your operating system (Windows, macOS, or Ubuntu).
   -Install the software following the instructions specific to your operating system.

2. Insert the SD Card into Your Computer
   -Insert your SD card into the SD card reader and connect it to your computer.

3. Open Raspberry Pi Imager
    -Launch the Raspberry Pi Imager application.

4. Select the OS
    -Click on `Choose OS`.
    -Select `Raspberry Pi OS (64-bit) Lite`. If you need a specific version or configuration, explore other options under          `Raspberry Pi OS (other)`.

5. Select the SD Card
    -Click on `Choose Storage`.
    -Select the SD card you inserted.

6. Configure Advanced Options
    -Click on the settings icon (gear icon) in the bottom right corner after selecting your OS and storage.
    -Enable SSH: Check the box "Enable SSH" and choose to use password authentication.
    -Set Username and Password: Enter a username and password for SSH access.  
    -Configure Wi-Fi: Enter your Wi-Fi SSID and password, and set the Wi-Fi country.
    -Set Locale Settings: Set the locale, timezone, and keyboard layout to match your preferences.
    -Save these settings by clicking “Save”.

7. Write the OS to the SD Card
    -Click on `Write`.
    -Confirm any prompts that appear, including entering your computer's admin password if required.
    -The imager will download the OS, write it to the SD card, and verify the write process. This can take several minutes.

8. Eject the SD Card
    -Once the writing process is complete, you will see a message indicating success.
    -Safely eject the SD card from your computer.

## II. Make Connections
1. Insert the SD Card into Raspberry Pi
2. Insert the newly flashed SD card into the SD card slot of your Raspberry Pi.
3. Insert Usb drive into USB port of raspberry pi.
4. Power On the Raspberry Pi
5. Connect the power supply to your Raspberry Pi to turn it on.

## III. Install Dependencies**
NOTE: If you have a monitor connected, you should see the Raspberry Pi OS booting up. In this case i am assuming that you are trying to estabilsh a headless setup
1. Install Software "Advanced IP Scanner" if do not have.
2. Open it and search "<RPI hostname>" in search bar. IP address of RPi will appear.
3. Open command prompt and execute ssh command:
        $ssh <username>@<ip>
  e.g. ssh pi@10.0.0.223

4. Execute bash script "get_started.sh" to update fimware.
5. Check with other basic linux commands
        ifconfig                      check ip of RPI
        df -h                         check disk usage
        free -m                       check RAM usage
        vcgencmd measure_temp         check the CPU temperature of a RPI
7. Environment is ready to start creating project.


