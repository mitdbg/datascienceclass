#!/bin/bash
for idx in {1..100}
do
  sudo userdel -r "user${idx}"
done
