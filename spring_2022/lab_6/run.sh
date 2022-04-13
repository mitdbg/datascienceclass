#!/bin/sh

file=lab6_reversed_lecture.ipynb
echo "\n>>>> Starting up jupyter notebook server...\n"
jupyter trust $file
jupyter notebook $file --ip 0.0.0.0 --port 8166 --no-browser --allow-root
