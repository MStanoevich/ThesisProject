#!/usr/bin/env bash
# run docker compose on images
images=$PWD/images-to-move-example  # folder with all of the images in
example_folder=$PWD/example  # proxy folder which one file will be moved to at a time
# NOTE: example_folder has to be set to the same folder as the :/pngs folder in ALL .yml files
# you plan on using

# clear example folder
rm -f $example_folder/*

# start of filename
fnStart="ffe-x264-savepngs"
# all of the different presets
declare -a presets=(
"faster"
"fast"
"medium"
"superfast"
"ultrafast"
"veryfast")

# two tunes
declare -a tunes=(
"ssim"
"pnsr")

# anotated and non anotated
anotated="anotated"
non_anotated="non_anotated"

# create all nessesary folders for all presets
for preset in ${presets[@]}; do
    for tune in ${tunes[@]}; do
        if [ ! -d $PWD/$preset-$tune-$anotated ]; then
            mkdir $PWD/$preset-$tune-$anotated
        fi
        if [ ! -d $PWD/$preset-$tune-$non_anotated ]; then
            mkdir $PWD/$preset-$tune-$non_anotated
        fi
        rm -f $preset-$tune-$anotated/*
        rm -f $preset-$tune-$non_anotated/*
    done
done

# enable xhost
xhost +
for preset in ${presets[@]}; do
    for tune in ${tunes[@]}; do
        echo "running preset $preset with tune $tune!"
        echo "file $file"
        docker-compose -f $fnStart"-"$preset"-"$tune"-"$anotated".yml" up &&  # run docker-compose on all different files
        rename 's/(l....\_)(0*)//' * &&  # rename files, removing lossy_ and 0s
        mogrify -format jpg -quality 100 *.png &&  # change format to jpg, 100% quality
        rm -f *.png && # removes old png images
        mv *.jpg  $preset-$tune-$anotated/
    done
done
