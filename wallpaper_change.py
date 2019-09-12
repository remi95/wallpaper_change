#!/usr/bin/python3.6

# Author: Rémi Mafat.
# This script is running by crontab.
# It randomly takes picture on images folder and put it on desktop wallpaper.

import os, random

imagesFolder = os.environ['HOME'] + "/Images/Wallpapers/"
images = os.listdir(imagesFolder)

def getRandomImage():
    randomImage = random.choice(images)
    return imagesFolder + randomImage

dbus_session_bus_address = 'PID=$(pgrep gnome-session | tail -n1) && export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-) && '
command = dbus_session_bus_address + 'gsettings set org.gnome.desktop.background picture-uri ' + getRandomImage()

os.system(command)
