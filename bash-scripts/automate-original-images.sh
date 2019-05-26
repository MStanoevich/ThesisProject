#!/usr/bin/env bash

# Place this file in darknet directory
# Make sure all paths used exist
# Make sure the labels/ folder has been copied from the original darknet repo into the data/ folder
# directory for jpg files, can be changed to an argument in later iterations

directory=$PWD/../../original-images

# start time variable
starttime=`date +%s`

# create directory if it doesnt exist
if [ ! -d $PWD/automate_results ]; then
    mkdir automate_results
fi

# set up variables for .data, .cfg and .weights file
d="$PWD/data/formula.data"
c="$PWD/cfg/formula.cfg"
w="$PWD/backup/formula_final.weights"

# loop through all png files
for filename in $directory/*.jpg; do
    # extract basename and basename with no extension
    bn=$(basename "$filename")
    nn=${bn%.jpg}
    # run command
    echo "running darknet on $bn" &&
    ./darknet detector test $d $c $w $filename > $nn.txt &&
    echo "done" &&
    sed -i '1,3d' $nn.txt && # remove first 3 lines of file

    # now, move the files to the correct location
    mv $nn.txt automate_results/ &&
    mv predictions.jpg automate_results/$bn

done

endtime=`date +%s`
echo "Total time to execute script: $((endtime-starttime)) seconds"
