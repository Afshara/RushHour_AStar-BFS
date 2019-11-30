#!/bin/sh
if [ "$#" -gt 1 ]; then
  python3 r.py "$1" "$2"

else
  python3 r.py "$1"

fi


