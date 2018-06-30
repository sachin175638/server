#!/bin/bash
echo ""
echo "Enter port :- "
read port

php -S localhost:$port /sdcard/hacking_server/instagram
