#!/bin/bash
gcc -o h2b2 h2b2.c
if [[$(user) == root]]; then
cp h2b2 /usr/local/bin/
else
sudo cp h2b2 /usr/local/bin/
fi
if [[$(user) == root]]; then
cp h2b2dump /usr/local/bin/
else
sudo cp h2b2dump /usr/local/bin/
fi
