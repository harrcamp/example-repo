#!/bin/bash

# If a directory named new_folder exists, create if_folder
if [ -d new_folder ]; then
    # -p prevents error if if_folder already exists
    mkdir -p if_folder
    # Let the user know we created it
    echo "Created directory 'if_folder'"
fi

# Check if if_folder exists; then create hyperionDev or new-projects
if [ -d if_folder ]; then
    mkdir -p hyperionDev
    echo "Created directory 'hyperionDev'"
else
    mkdir -p new-projects
    echo "Created directory 'new-projects'"
fi
 