#!/bin/bash
echo -n "Enter ip or domain :- "
read ip
echo -n "Entet port :- "
read port
echo -n "file name :- "
read file
php -S $ip:$port -t /sdcard/$file
