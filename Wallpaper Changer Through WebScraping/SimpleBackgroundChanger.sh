#!/bin/bash

#PID=$(pgrep gnome-session)
#export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

python3 DailyQouteFromInternet.py

cp /home/khalid/Documents/Python\ Web\ Scrapers/Wallpaper\ Changer\ Through\ WebScraping/img.jpg /home/khalid/Pictures/

rm newimg img.jpg

DIR="/home/khalid/Pictures/img.jpg"

#PIC=$(ls $DIR/* | shuf -n1)

gsettings set org.gnome.desktop.background picture-uri "file://$DIR"

#gsettings set org.gnome.desktop.background picture-uri 'file:///home/khalid/Pictures/img'
