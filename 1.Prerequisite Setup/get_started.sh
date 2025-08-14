#!/bin/bash

# Step 4: Update firmware
echo "Updating firmware..."
sudo rpi-update -y
sleep 3

# Step 5: Update the list of available packages
echo "Updating package list..."
sudo apt update
sleep 3

# Step 6: See list of updated packages
echo "Listing upgradable packages..."
sudo apt list --upgradable
sleep 3

# Step 7: Upgrade all installed packages to their latest versions
echo "Upgrading all packages..."
sudo apt full-upgrade -y
sleep 3
