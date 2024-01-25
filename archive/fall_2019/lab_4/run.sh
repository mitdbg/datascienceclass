#!/bin/sh

echo "\n>>>> Starting up jupyter notebook server...\n"
jupyter trust ML_reverse_lecture.ipynb
jupyter notebook ML_reverse_lecture.ipynb --ip 0.0.0.0 --port 8888 --no-browser --allow-root
