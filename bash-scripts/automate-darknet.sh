#!/usr/bin/env bash
# Place this file in darknet directory
# Make sure all paths used exist
# Make sure the labels/ folder has been copied from the original darknet repo into the data/ folder
# FFE path
ffePath=/home/jonathan/Documents/Thesis/frame-feed-evaluator
darknetPath=/home/jonathan/Documents/Thesis/yolo-perception-master/darknet
# darknet path
originalImages="./data/anotated"
declare -a presetPaths=(
"../../frame-feed-evaluator/fast-pnsr-anotated"
"../../frame-feed-evaluator/fast-ssim-anotated"
"../../frame-feed-evaluator/faster-pnsr-anotated"
"../../frame-feed-evaluator/faster-ssim-anotated"
"../../frame-feed-evaluator/medium-pnsr-anotated"
"../../frame-feed-evaluator/medium-ssim-anotated"
"../../frame-feed-evaluator/superfast-pnsr-anotated"
"../../frame-feed-evaluator/superfast-ssim-anotated"
"../../frame-feed-evaluator/ultrafast-pnsr-anotated"
"../../frame-feed-evaluator/ultrafast-ssim-anotated"
"../../frame-feed-evaluator/veryfast-pnsr-anotated"
"../../frame-feed-evaluator/veryfast-ssim-anotated"
)
declare -a presetNames=(
"fast-pnsr"
"fast-ssim"
"faster-pnsr"
"faster-ssim"
"medium-pnsr"
"medium-ssim"
"superfast-pnsr"
"superfast-ssim"
"ultrafast-pnsr"
"ultrafast-ssim"
"veryfast-pnsr"
"veryfast-ssim"
)
# start time variable
starttime=`date +%s`

# function for automation
darknet_execution() { # $1 = path $2 = name of encoding
    echo "darknet execution"
    # create directory for preset
    if [ ! -d $2/automate_results ]; then
        mkdir $PWD/$2

    fi
    data="data/formula.data"
    config="cfg/formula.cfg"
    weights="backup/formula_final.weights"

    # loop through files in preset dir
    for filename in $1/*.jpg; do
        bn=$(basename "$filename")
        nn=${bn%.jpg}
        #run darknet on files
        echo "running darknet on $bn" &&
        ./darknet detector test $data $config $weights $filename > $nn.txt &&
        echo "done" &&
        sed -i '1,3d' $nn.txt && # remove first 3 lines of files
        mv predictions.jpg $2/$bn
        mv $nn.txt $2/$nn.txt
    done
}
counter=0
# directory for jpg files, probably shoud be $PWD/data/anotated/*.jpg
directory=$PWD/data/images_to_check/*.jpg

# first, run ffe
cd $ffePath
./automate.sh # run ffe automation
cd $darknetPath
# run darknet on everything
for preset in ${presetPaths[@]}; do
    darknet_execution $preset ${presetNames[$counter]}
    counter=$((counter+1))
done


endtime=`date +%s`
echo "Total time to execute script: $((endtime-starttime)) seconds"
