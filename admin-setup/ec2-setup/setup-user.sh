#!/bin/bash

for idx in {1..100}
do
  # correct permissions on key file
  chmod 400 "ssh-keys/user${idx}.pem"

  # create user
  sudo adduser "user${idx}" --disabled-password --gecos ""

  # store public key
  pubkey=`ssh-keygen -y -f "ssh-keys/user${idx}.pem"`

  # add public key to authorized users
  sudo su "user${idx}" -c "mkdir /home/user${idx}/.ssh"
  sudo su "user${idx}" -c "chmod 700 /home/user${idx}/.ssh"
  sudo su "user${idx}" -c "touch /home/user${idx}/.ssh/authorized_keys"
  sudo su "user${idx}" -c "chmod 600 /home/user${idx}/.ssh/authorized_keys"
  sudo su "user${idx}" -c "echo ${pubkey} > /home/user${idx}/.ssh/authorized_keys"
done


