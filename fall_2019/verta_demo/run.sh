#!/bin/sh

file=census-end-to-end-s3-example-mit-class.ipynb
echo "\n>>>> Starting up jupyter notebook server...\n"
jupyter trust $file
jupyter notebook $file --ip 0.0.0.0 --port 8166 --no-browser --allow-root
