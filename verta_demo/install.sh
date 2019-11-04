#!/bin/sh

echo "\n>>>> Installing python packages...\n"
pip3 install -r requirements.txt

echo "\n>>>> Installing wget..."
apt install -y wget

#echo "\n>>>> Unzipping spotify_songs.zip...\n"
#apt install -y unzip wget
#c=`pwd`
#cd data/; unzip data.zip; cd $c
