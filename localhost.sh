#!/bin/bash
figlet localHost
echo -n "Enter port :- "
read port
echo -n "Enter file name :- "
read file
php -S localhost:$port -t /sdcard/$file
