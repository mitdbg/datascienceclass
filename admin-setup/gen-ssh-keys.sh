#!/bin/bash
for idx in {1..60}
do
  aws ec2 create-key-pair --key-name "user${idx}" --key-type ed25519 --key-format pem --query "KeyMaterial" --output text > "ssh-keys/user${idx}.pem"
done
