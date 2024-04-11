#!/usr/bin/bash
random_filename=`cat /dev/urandom | tr -cd 'a-f0-9' | head -c 32`.py
cat $1  > $random_filename

scp -i key.pem $random_filename hadoop@ec2-13-58-234-100.us-east-2.compute.amazonaws.com:/home/hadoop/
ssh -i key.pem hadoop@ec2-13-58-234-100.us-east-2.compute.amazonaws.com "spark-submit --master yarn /home/hadoop/$random_filename; rm /home/hadoop/$random_filename" > $1.stdout  2> $1.stderr
rm $random_filename