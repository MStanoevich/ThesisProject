# How to use the script
a certain folder structure is required for the script to work as intended.

```
project folder
│
└───yolo-perception-master
│   │
│   └───darknet
|       |   automate-original-images.sh
│       |   ...
|
└───data
    └───anotated
    └───non-anotated
```

1. Move `automate-darknet.sh` to the darknet folder.
2. Execute `automate-darknet.sh` which will create new directories containing the results. 

    It is important that you ensure that the variables in these scripts that contain
    paths are correct, or else it will not work.

