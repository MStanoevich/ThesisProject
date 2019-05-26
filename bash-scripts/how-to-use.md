# How to use the scripts
a certain folder structure is required for the scripts to interact properly with
each other

```
project folder
│
└───yolo-perception-master
│   │
│   └───darknet
|       |   automate-original-images.sh
│       │   automate-darknet.sh
│       |   ...
|
└───frame-feed-evaluator
    │   automate-ffe.sh
    |   ...
```

1. Move to the frame-feed-evaluator folder and run the `automate-ffe.sh` script.

   This will create folders for all the presets and tunes with all images to be
placed in

2. Move to the darknet subfolder. Here you will find two scripts, execute `automate-darknet.sh`
to run the darknet algorithm on the images created by ffe, or `automate-original-images.sh` to run it on
the original, uncompressed images

    It is important that you ensure that the variables in these scripts that contain
    paths are correct, or else it will not work.

    For `automate-original-images.sh`, this script is for the original uncompressed data, however
    this data is in png format and is therefore not supported by darknet. To change the format into
    jpg you can run the following in the directory that contains the original images: `mogrify -format jpg -quality 100 *.png`
