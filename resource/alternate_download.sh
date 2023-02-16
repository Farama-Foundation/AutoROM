#!/bin/bash

echo $DUMMY_KEY
echo $DUMMY_KEY
echo $DUMMY_KEY
echo $DUMMY_KEY
echo $DUMMY_KEY
echo $DUMMY_KEY
exit
wget https://raw.githubusercontent.com/jjshoots/AutoROM/master/resource/Roms.tar.gz.b64.enc
openssl aes-256-cbc -a -salt -pass pass:$DECRYPTION_KEY -in Roms.tar.gz.b64.enc -out Roms.tar.gz.b64 -d
base64 Roms.tar.gz.b64 --decode &> Roms.tar.gz
