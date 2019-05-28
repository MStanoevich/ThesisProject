# Extract metrics out of results
import csv

def percentage(a, b):
    return round(a / b * 100, 2)

total_original_confidence = 0

total_ufSSIM_confidence = 0
total_ufPNSR_confidence = 0

total_sfSSIM_confidence = 0
total_sfPNSR_confidence = 0

total_vfSSIM_confidence = 0
total_vfPNSR_confidence = 0

total_ferSSIM_confidence = 0
total_ferPNSR_confidence = 0

total_fSSIM_confidence = 0
total_fPNSR_confidence = 0

total_mSSIM_confidence = 0
total_mPNSR_confidence = 0

with open("h264_results/results_confidence.csv") as f:
    for row in csv.reader(f):
        total_original_confidence += int(row[1])
        total_ufSSIM_confidence += int(row[2])
        total_ufPNSR_confidence += int(row[3])
        total_sfSSIM_confidence += int(row[4])
        total_sfPNSR_confidence += int(row[5])
        total_vfSSIM_confidence += int(row[6])
        total_vfPNSR_confidence += int(row[7])
        total_ferSSIM_confidence += int(row[8])
        total_ferPNSR_confidence += int(row[9])
        total_fSSIM_confidence += int(row[10])
        total_fPNSR_confidence += int(row[11])
        total_mSSIM_confidence += int(row[12])
        total_mPNSR_confidence += int(row[13])

total_original_size = 0

total_ufSSIM_size = 0
total_ufPNSR_size = 0

total_sfSSIM_size = 0
total_sfPNSR_size = 0

total_vfSSIM_size = 0
total_vfPNSR_size = 0

total_ferSSIM_size = 0
total_ferPNSR_size = 0

total_fSSIM_size = 0
total_fPNSR_size = 0

total_mSSIM_size = 0
total_mPNSR_size = 0

with open("h264_results/results_size.csv") as f:
        for row in csv.reader(f):
            total_original_size += int(row[0])
            total_ufSSIM_size += int(row[1])
            total_ufPNSR_size += int(row[2])
            total_sfSSIM_size += int(row[3])
            total_sfPNSR_size += int(row[4])
            total_vfSSIM_size += int(row[5])
            total_vfPNSR_size += int(row[6])
            total_ferSSIM_size += int(row[7])
            total_ferPNSR_size += int(row[8])
            total_fSSIM_size += int(row[9])
            total_fPNSR_size += int(row[10])
            total_mSSIM_size += int(row[11])
            total_mPNSR_size += int(row[12])

# Metrics
ufSSIM_confidence = percentage(total_ufSSIM_confidence, total_original_confidence)
ufSSIM_size = percentage(total_ufSSIM_size, total_original_size)

ufPNSR_confidence = percentage(total_ufPNSR_confidence, total_original_confidence)
ufPNSR_size = percentage(total_ufPNSR_size, total_original_size)

sfSSIM_confidence = percentage(total_sfSSIM_confidence, total_original_confidence)
sfSSIM_size = percentage(total_sfSSIM_size, total_original_size)

sfPNSR_confidence = percentage(total_sfPNSR_confidence, total_original_confidence)
sfPNSR_size = percentage(total_sfPNSR_size, total_original_size)

vfSSIM_confidence = percentage(total_vfSSIM_confidence, total_original_confidence)
vfSSIM_size = percentage(total_vfSSIM_size, total_original_size)

vfPNSR_confidence = percentage(total_vfPNSR_confidence, total_original_confidence)
vfPNSR_size = percentage(total_vfPNSR_size, total_original_size)

ferSSIM_confidence = percentage(total_ferSSIM_confidence, total_original_confidence)
ferSSIM_size = percentage(total_ferSSIM_size, total_original_size)

ferPNSR_confidence = percentage(total_ferPNSR_confidence, total_original_confidence)
ferPNSR_size = percentage(total_ferPNSR_size, total_original_size)

fSSIM_confidence = percentage(total_fSSIM_confidence, total_original_confidence)
fSSIM_size = percentage(total_fSSIM_size, total_original_size)

fPNSR_confidence = percentage(total_fPNSR_confidence, total_original_confidence)
fPNSR_size = percentage(total_fPNSR_size, total_original_size)

mSSIM_confidence = percentage(total_mSSIM_confidence, total_original_confidence)
mSSIM_size = percentage(total_mSSIM_size, total_original_size)

mPNSR_confidence = percentage(total_mPNSR_confidence, total_original_confidence)
mPNSR_size = percentage(total_mPNSR_size, total_original_size)

extracted_metrics = open("h264_results/extracted_metrics.csv", "w+")
extracted_metrics.write("codec, NN performance compared to original, File size when compared to original, K metric\n"
    + "h264-ultrafastSSIM," + str(ufSSIM_confidence) + "," + str(ufSSIM_size) + "," + str(round(ufSSIM_confidence/ufSSIM_size,2)) + "\n"
    + "h264-ultrafastPNSR," + str(ufPNSR_confidence) + "," + str(ufPNSR_size) + "," + str(round(ufPNSR_confidence/ufPNSR_size,2)) + "\n"
    + "h264-superfastSSIM," + str(sfSSIM_confidence) + "," + str(sfSSIM_size) + "," + str(round(sfSSIM_confidence/sfSSIM_size,2)) + "\n"
    + "h264-superfastPNSR," + str(sfPNSR_confidence) + "," + str(sfPNSR_size) + "," + str(round(sfPNSR_confidence/sfPNSR_size,2)) + "\n"
    + "h264-veryfastSSIM," + str(vfSSIM_confidence) + "," + str(vfSSIM_size) + "," + str(round(vfSSIM_confidence/vfSSIM_size,2)) + "\n"
    + "h264-veryfastPNSR," + str(vfPNSR_confidence) + "," + str(vfPNSR_size) + "," + str(round(vfPNSR_confidence/vfPNSR_size,2)) + "\n"
    + "h264-fasterSSIM," + str(ferSSIM_confidence) + "," + str(ferSSIM_size) + "," + str(round(ferSSIM_confidence/ferSSIM_size,2)) + "\n"
    + "h264-fasterPNSR," + str(ferPNSR_confidence) + "," + str(ferPNSR_size) + "," + str(round(ferPNSR_confidence/ferPNSR_size,2)) + "\n"
    + "h264-fastSSIM," + str(fSSIM_confidence) + "," + str(fSSIM_size) + "," + str(round(fSSIM_confidence/fSSIM_size,2)) + "\n"
    + "h264-fastPNSR," + str(fPNSR_confidence) + "," + str(fPNSR_size) + "," + str(round(fPNSR_confidence/fPNSR_size,2)) + "\n"
    + "h264-mediumSSIM," + str(mSSIM_confidence) + "," + str(mSSIM_size) + "," + str(round(mSSIM_confidence/mSSIM_size,2)) + "\n"
    + "h264-mediumPNSR," + str(mPNSR_confidence) + "," + str(mPNSR_size) + "," + str(round(mPNSR_confidence/mPNSR_size,2)))

k_metrics_for_plotting = open("h264_results/k_metrics_for_plotting.csv", "w+")
k_metrics_for_plotting.write("h264-ufSSIM,h264-ufPNSR,h264-sfSSIM,h264-sfPNSR,h264-vfSSIM,h264-vfPNSR,h264-ferSSIM,h264-ferPNSR,h264-fSSIM,h265-fPNSR,h264-mSSIM,h264-mPNSR\n" 
    + str(round(ufSSIM_confidence/ufSSIM_size,2)) + "," + str(round(ufPNSR_confidence/ufPNSR_size,2)) + "," 
    + str(round(sfSSIM_confidence/sfSSIM_size,2)) + "," + str(round(sfPNSR_confidence/sfPNSR_size,2)) + ","
    + str(round(vfSSIM_confidence/vfSSIM_size,2)) + "," + str(round(vfPNSR_confidence/vfPNSR_size,2)) + ","
    + str(round(ferSSIM_confidence/ferSSIM_size,2)) + "," + str(round(ferPNSR_confidence/ferPNSR_size,2)) + ","
    + str(round(fSSIM_confidence/fSSIM_size,2)) + "," + str(round(fPNSR_confidence/fPNSR_size,2)) + "," 
    + str(round(mSSIM_confidence/mSSIM_size,2)) + "," + str(round(mPNSR_confidence/mPNSR_size,2)))

confidence_metrics_for_plotting = open("h264_results/confidence_metrics_for_plotting.csv", "w+")
confidence_metrics_for_plotting.write("h264-ufSSIM,h264-ufPNSR,h264-sfSSIM,h264-sfPNSR,h264-vfSSIM,h264-vfPNSR,h264-ferSSIM,h264-ferPNSR,h264-fSSIM,h265-fPNSR,h264-mSSIM,h264-mPNSR\n"
    + str(ufSSIM_confidence) + "," + str(ufPNSR_confidence) + "," + str(sfSSIM_confidence) + "," + str(sfPNSR_confidence) + "," 
    + str(vfSSIM_confidence) + "," + str(vfPNSR_confidence) + "," + str(ferSSIM_confidence) + "," + str(ferPNSR_confidence) + ","
    + str(fSSIM_confidence) + "," + str(fPNSR_confidence) + "," + str(mSSIM_confidence) + "," + str(mPNSR_confidence))

size_metrics_for_plotting = open("h264_results/size_metrics_for_plotting.csv", "w+")
size_metrics_for_plotting.write("h264-ufSSIM,h264-ufPNSR,h264-sfSSIM,h264-sfPNSR,h264-vfSSIM,h264-vfPNSR,h264-ferSSIM,h264-ferPNSR,h264-fSSIM,h265-fPNSR,h264-mSSIM,h264-mPNSR\n"
    + str(ufSSIM_size) + "," + str(ufPNSR_size) + "," + str(sfSSIM_size) + "," + str(sfPNSR_size) + "," 
    + str(vfSSIM_size) + "," + str(vfPNSR_size) + "," + str(ferSSIM_size) + "," + str(ferPNSR_size) + ","
    + str(fSSIM_size) + "," + str(fPNSR_size) + "," + str(mSSIM_size) + "," + str(mPNSR_size))