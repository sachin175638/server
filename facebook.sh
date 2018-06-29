#!/bin/bash
echo -n "Enter port :- "
read port
php -S localhost:$port -t /sdcard/hacking_server/facebook/php
