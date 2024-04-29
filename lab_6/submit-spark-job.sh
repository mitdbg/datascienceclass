#!/usr/bin/bash
random_filename=`cat /dev/urandom | tr -cd 'a-f0-9' | head -c 32`.py
cat $1  > $random_filename

scp -o StrictHostKeyChecking=no -i key.pem $random_filename hadoop@ec2-18-216-4-88.us-east-2.compute.amazonaws.com:/home/hadoop/
ssh -o StrictHostKeyChecking=no -i key.pem hadoop@ec2-18-216-4-88.us-east-2.compute.amazonaws.com "spark-submit --master yarn /home/hadoop/$random_filename; rm /home/hadoop/$random_filename" > $1.stdout  2> $1.stderr
rm $random_filename
