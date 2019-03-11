#!/bin/bash
# Script to clean the tree from all compiled files.
# You can rebuild them afterwards using "build.sh".
# Written by Juan Rios, 3/10/2019

# Remove the dedicated output directories
cd `dirname $0`

rm -rf build

# We're done!
echo Cleaned up the project!