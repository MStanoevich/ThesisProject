#!/usr/bin/env bash
# Place this file in darknet directory
# Make sure all paths used exist
# Make sure the labels/ folder has been copied from the original darknet repo into the data/ folder
darknetPath=/home/marko/Thesis/yolo-perception/darknet
# darknet path
declare -a presetPaths=(
"../../data/ffmpeg/non_anotated/original_from_video"
"../../data/ffmpeg/non_anotated/ufSSIM"
"../../data/ffmpeg/non_anotated/ufPSNR"
"../../data/ffmpeg/non_anotated/sfSSIM"
"../../data/ffmpeg/non_anotated/sfPSNR"
"../../data/ffmpeg/non_anotated/vfSSIM"
"../../data/ffmpeg/non_anotated/vfPSNR"
"../../data/ffmpeg/non_anotated/ferSSIM"
"../../data/ffmpeg/non_anotated/ferPSNR"
"../../data/ffmpeg/non_anotated/fSSIM"
"../../data/ffmpeg/non_anotated/fPSNR"
"../../data/ffmpeg/non_anotated/mSSIM"
"../../data/ffmpeg/non_anotated/mPSNR"
"../../data/ffmpeg/non_anotated/sSSIM"
"../../data/ffmpeg/non_anotated/sPSNR"
"../../data/ffmpeg/non_anotated/serSSIM"
"../../data/ffmpeg/non_anotated/serPSNR"
"../../data/ffmpeg/non_anotated/vsSSIM"
"../../data/ffmpeg/non_anotated/vsPSNR"
)
declare -a presetNames=(
"original-from-video"
"ultrafast-ssim"
"ultrafast-psnr"
"superfast-ssim"
"superfast-psnr"
"veryfast-ssim"
"veryfast-psnr"
"faster-ssim"
"faster-psnr"
"fast-ssim"
"fast-psnr"
"medium-ssim"
"medium-psnr"
"slow-ssim"
"slow-psnr"
"slower-ssim"
"slower-psnr"
"veryslow-ssim"
"veryslow-psnr"
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

cd $darknetPath
# run darknet on everything
for preset in ${presetPaths[@]}; do
    darknet_execution $preset ${presetNames[$counter]}
    counter=$((counter+1))
done


endtime=`date +%s`
echo "Total time to execute script: $((endtime-starttime)) seconds"
