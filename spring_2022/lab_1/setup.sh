#!/bin/bash

apt install -y wget zip unzip

outputname=data
url=https://muimages.sfo2.digitaloceanspaces.com/data.zip

wget -O ${outputname}.zip ${url} 
unzip ${outputname}.zip