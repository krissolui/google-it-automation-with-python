#!/bin/bash

> oldFiles.txt

files=$(grep ' jane ' ~/data/list.txt | cut -d ' ' -f 3)

for file in $files
do
        if test -e "$HOME$file";
        then
                echo "$file exists"
                readlink -m "$HOME$file" >> oldFiles.txt
        fi
done