#!bin/bash

djlint . --reformat --format-css --format-js
black . -v --diff