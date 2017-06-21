#!/bin/bash

for FILE in ./*/*.py; do
  echo -----$FILE-----
  python3 $FILE
done
