#!/bin/sh

echo "\n>>>> Starting up jupyter notebook server...\n"
jupyter notebook lab5_reversed_lecture.ipynb --ip 0.0.0.0 --port 8166 --no-browser --allow-root
