#!/bin/bash

# Create three top-level directories named dirA, dirB, and dirC.
mkdir -p dirA dirB dirC

# Navigate into one of the directories (dirA) to perform nested operations.
cd dirA || exit

# Create three subdirectories inside dirA: sub1, sub2, and sub3.
mkdir -p sub1 sub2 sub3

# Remove two of the subdirectories (sub2 and sub3) as required.
rmdir sub2 sub3
