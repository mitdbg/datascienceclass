#!/bin/bash
for idx in {1..60}
do
  sudo userdel -r "user${idx}"
done
