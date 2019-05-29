# Extract metrics out of results
import csv

def percentage(a, b):
    return round(a / b * 100, 2)

total_original_confidence = 0

total_ufSSIM_confidence = 0
total_ufPSNR_confidence = 0

total_sfSSIM_confidence = 0
total_sfPSNR_confidence = 0

total_vfSSIM_confidence = 0
total_vfPSNR_confidence = 0

total_ferSSIM_confidence = 0
total_ferPSNR_confidence = 0

total_fSSIM_confidence = 0
total_fPSNR_confidence = 0

total_mSSIM_confidence = 0
total_mPSNR_confidence = 0

total_sSSIM_confidence = 0
total_sPSNR_confidence = 0

total_serSSIM_confidence = 0
total_serPSNR_confidence = 0

total_vsSSIM_confidence = 0
total_vsPSNR_confidence = 0

with open("h264_results/results_confidence.csv") as f:
    for row in csv.reader(f):
        total_original_confidence += int(row[1])
        total_ufSSIM_confidence += int(row[2])
        total_ufPSNR_confidence += int(row[3])
        total_sfSSIM_confidence += int(row[4])
        total_sfPSNR_confidence += int(row[5])
        total_vfSSIM_confidence += int(row[6])
        total_vfPSNR_confidence += int(row[7])
        total_ferSSIM_confidence += int(row[8])
        total_ferPSNR_confidence += int(row[9])
        total_fSSIM_confidence += int(row[10])
        total_fPSNR_confidence += int(row[11])
        total_mSSIM_confidence += int(row[12])
        total_mPSNR_confidence += int(row[13])
        total_sSSIM_confidence += int(row[14])
        total_sPSNR_confidence += int(row[15])
        total_serSSIM_confidence += int(row[16])
        total_serPSNR_confidence += int(row[17])
        total_vsSSIM_confidence += int(row[18])
        total_vsPSNR_confidence += int(row[19])

total_original_size = 0

total_ufSSIM_size = 0
total_ufPSNR_size = 0

total_sfSSIM_size = 0
total_sfPSNR_size = 0

total_vfSSIM_size = 0
total_vfPSNR_size = 0

total_ferSSIM_size = 0
total_ferPSNR_size = 0

total_fSSIM_size = 0
total_fPSNR_size = 0

total_mSSIM_size = 0
total_mPSNR_size = 0

total_sSSIM_size = 0
total_sPSNR_size = 0

total_serSSIM_size = 0
total_serPSNR_size = 0

total_vsSSIM_size = 0
total_vsPSNR_size = 0

with open("h264_results/results_size.csv") as f:
        for row in csv.reader(f):
            total_original_size += int(row[0])
            total_ufSSIM_size += int(row[1])
            total_ufPSNR_size += int(row[2])
            total_sfSSIM_size += int(row[3])
            total_sfPSNR_size += int(row[4])
            total_vfSSIM_size += int(row[5])
            total_vfPSNR_size += int(row[6])
            total_ferSSIM_size += int(row[7])
            total_ferPSNR_size += int(row[8])
            total_fSSIM_size += int(row[9])
            total_fPSNR_size += int(row[10])
            total_mSSIM_size += int(row[11])
            total_mPSNR_size += int(row[12])
            total_sSSIM_size += int(row[13])
            total_sPSNR_size += int(row[14])
            total_serSSIM_size += int(row[15])
            total_serPSNR_size += int(row[16])
            total_vsSSIM_size += int(row[17])
            total_vsPSNR_size += int(row[18])

# Metrics
ufSSIM_confidence = percentage(total_ufSSIM_confidence, total_original_confidence)
ufSSIM_size = percentage(total_ufSSIM_size, total_original_size)

ufPSNR_confidence = percentage(total_ufPSNR_confidence, total_original_confidence)
ufPSNR_size = percentage(total_ufPSNR_size, total_original_size)

sfSSIM_confidence = percentage(total_sfSSIM_confidence, total_original_confidence)
sfSSIM_size = percentage(total_sfSSIM_size, total_original_size)

sfPSNR_confidence = percentage(total_sfPSNR_confidence, total_original_confidence)
sfPSNR_size = percentage(total_sfPSNR_size, total_original_size)

vfSSIM_confidence = percentage(total_vfSSIM_confidence, total_original_confidence)
vfSSIM_size = percentage(total_vfSSIM_size, total_original_size)

vfPSNR_confidence = percentage(total_vfPSNR_confidence, total_original_confidence)
vfPSNR_size = percentage(total_vfPSNR_size, total_original_size)

ferSSIM_confidence = percentage(total_ferSSIM_confidence, total_original_confidence)
ferSSIM_size = percentage(total_ferSSIM_size, total_original_size)

ferPSNR_confidence = percentage(total_ferPSNR_confidence, total_original_confidence)
ferPSNR_size = percentage(total_ferPSNR_size, total_original_size)

fSSIM_confidence = percentage(total_fSSIM_confidence, total_original_confidence)
fSSIM_size = percentage(total_fSSIM_size, total_original_size)

fPSNR_confidence = percentage(total_fPSNR_confidence, total_original_confidence)
fPSNR_size = percentage(total_fPSNR_size, total_original_size)

mSSIM_confidence = percentage(total_mSSIM_confidence, total_original_confidence)
mSSIM_size = percentage(total_mSSIM_size, total_original_size)

mPSNR_confidence = percentage(total_mPSNR_confidence, total_original_confidence)
mPSNR_size = percentage(total_mPSNR_size, total_original_size)

sSSIM_confidence = percentage(total_sSSIM_confidence, total_original_confidence)
sSSIM_size = percentage(total_sSSIM_size, total_original_size)

sPSNR_confidence = percentage(total_sPSNR_confidence, total_original_confidence)
sPSNR_size = percentage(total_sPSNR_size, total_original_size)

serSSIM_confidence = percentage(total_serSSIM_confidence, total_original_confidence)
serSSIM_size = percentage(total_serSSIM_size, total_original_size)

serPSNR_confidence = percentage(total_serPSNR_confidence, total_original_confidence)
serPSNR_size = percentage(total_serPSNR_size, total_original_size)

vsSSIM_confidence = percentage(total_vsSSIM_confidence, total_original_confidence)
vsSSIM_size = percentage(total_vsSSIM_size, total_original_size)

vsPSNR_confidence = percentage(total_vsPSNR_confidence, total_original_confidence)
vsPSNR_size = percentage(total_vsPSNR_size, total_original_size)


extracted_metrics = open("h264_results/extracted_metrics.csv", "w+")
extracted_metrics.write("codec, NN performance compared to original, File size when compared to original, K metric\n"
    + "h264-ultrafastSSIM," + str(ufSSIM_confidence) + "," + str(ufSSIM_size) + "," + str(round(ufSSIM_confidence/ufSSIM_size,2)) + "\n"
    + "h264-ultrafastPSNR," + str(ufPSNR_confidence) + "," + str(ufPSNR_size) + "," + str(round(ufPSNR_confidence/ufPSNR_size,2)) + "\n"
    + "h264-superfastSSIM," + str(sfSSIM_confidence) + "," + str(sfSSIM_size) + "," + str(round(sfSSIM_confidence/sfSSIM_size,2)) + "\n"
    + "h264-superfastPSNR," + str(sfPSNR_confidence) + "," + str(sfPSNR_size) + "," + str(round(sfPSNR_confidence/sfPSNR_size,2)) + "\n"
    + "h264-veryfastSSIM," + str(vfSSIM_confidence) + "," + str(vfSSIM_size) + "," + str(round(vfSSIM_confidence/vfSSIM_size,2)) + "\n"
    + "h264-veryfastPSNR," + str(vfPSNR_confidence) + "," + str(vfPSNR_size) + "," + str(round(vfPSNR_confidence/vfPSNR_size,2)) + "\n"
    + "h264-fasterSSIM," + str(ferSSIM_confidence) + "," + str(ferSSIM_size) + "," + str(round(ferSSIM_confidence/ferSSIM_size,2)) + "\n"
    + "h264-fasterPSNR," + str(ferPSNR_confidence) + "," + str(ferPSNR_size) + "," + str(round(ferPSNR_confidence/ferPSNR_size,2)) + "\n"
    + "h264-fastSSIM," + str(fSSIM_confidence) + "," + str(fSSIM_size) + "," + str(round(fSSIM_confidence/fSSIM_size,2)) + "\n"
    + "h264-fastPSNR," + str(fPSNR_confidence) + "," + str(fPSNR_size) + "," + str(round(fPSNR_confidence/fPSNR_size,2)) + "\n"
    + "h264-mediumSSIM," + str(mSSIM_confidence) + "," + str(mSSIM_size) + "," + str(round(mSSIM_confidence/mSSIM_size,2)) + "\n"
    + "h264-mediumPSNR," + str(mPSNR_confidence) + "," + str(mPSNR_size) + "," + str(round(mPSNR_confidence/mPSNR_size,2)) + "\n"
    + "h264-slowSSIM," + str(sSSIM_confidence) + "," + str(sSSIM_size) + "," + str(round(sSSIM_confidence/sSSIM_size,2)) + "\n"
    + "h264-slowPSNR," + str(sPSNR_confidence) + "," + str(sPSNR_size) + "," + str(round(sPSNR_confidence/sPSNR_size,2)) + "\n"
    + "h264-slowerSSIM," + str(serSSIM_confidence) + "," + str(serSSIM_size) + "," + str(round(serSSIM_confidence/serSSIM_size,2)) + "\n"
    + "h264-slowerPSNR," + str(serPSNR_confidence) + "," + str(serPSNR_size) + "," + str(round(serPSNR_confidence/serPSNR_size,2)) + "\n"
    + "h264-veryslowSSIM," + str(vsSSIM_confidence) + "," + str(vsSSIM_size) + "," + str(round(vsSSIM_confidence/vsSSIM_size,2)) + "\n"
    + "h264-veryslowPSNR," + str(vsPSNR_confidence) + "," + str(vsPSNR_size) + "," + str(round(vsPSNR_confidence/vsPSNR_size,2)))

k_metrics_for_plotting = open("h264_results/k_metrics_for_plotting.csv", "w+")
k_metrics_for_plotting.write("h264-ufSSIM,h264-ufPSNR,h264-sfSSIM,h264-sfPSNR,h264-vfSSIM,h264-vfPSNR,h264-ferSSIM,h264-ferPSNR,h264-fSSIM,h265-fPSNR,h264-mSSIM,h264-mPSNR\n" 
    + str(round(ufSSIM_confidence/ufSSIM_size,2)) + "," + str(round(ufPSNR_confidence/ufPSNR_size,2)) + "," 
    + str(round(sfSSIM_confidence/sfSSIM_size,2)) + "," + str(round(sfPSNR_confidence/sfPSNR_size,2)) + ","
    + str(round(vfSSIM_confidence/vfSSIM_size,2)) + "," + str(round(vfPSNR_confidence/vfPSNR_size,2)) + ","
    + str(round(ferSSIM_confidence/ferSSIM_size,2)) + "," + str(round(ferPSNR_confidence/ferPSNR_size,2)) + ","
    + str(round(fSSIM_confidence/fSSIM_size,2)) + "," + str(round(fPSNR_confidence/fPSNR_size,2)) + "," 
    + str(round(mSSIM_confidence/mSSIM_size,2)) + "," + str(round(mPSNR_confidence/mPSNR_size,2)) + ","
    + str(round(sSSIM_confidence/sSSIM_size,2)) + "," + str(round(sPSNR_confidence/sPSNR_size,2)) + ","
    + str(round(serSSIM_confidence/serSSIM_size,2)) + "," + str(round(serPSNR_confidence/serPSNR_size,2)) + ","
    + str(round(vsSSIM_confidence/vsSSIM_size,2)) + "," + str(round(vsPSNR_confidence/vsPSNR_size,2)))

confidence_metrics_for_plotting = open("h264_results/confidence_metrics_for_plotting.csv", "w+")
confidence_metrics_for_plotting.write("h264-ufSSIM,h264-ufPSNR,h264-sfSSIM,h264-sfPSNR,h264-vfSSIM,h264-vfPSNR,h264-ferSSIM,h264-ferPSNR,h264-fSSIM,h265-fPSNR,h264-mSSIM,h264-mPSNR\n"
    + str(ufSSIM_confidence) + "," + str(ufPSNR_confidence) + "," + str(sfSSIM_confidence) + "," + str(sfPSNR_confidence) + "," 
    + str(vfSSIM_confidence) + "," + str(vfPSNR_confidence) + "," + str(ferSSIM_confidence) + "," + str(ferPSNR_confidence) + ","
    + str(fSSIM_confidence) + "," + str(fPSNR_confidence) + "," + str(mSSIM_confidence) + "," + str(mPSNR_confidence) + ","
    + str(sSSIM_confidence) + "," + str(sPSNR_confidence) + "," + str(serSSIM_confidence) + "," + str(serPSNR_confidence) + ","
    + str(vsSSIM_confidence) + "," + str(vsPSNR_confidence))

size_metrics_for_plotting = open("h264_results/size_metrics_for_plotting.csv", "w+")
size_metrics_for_plotting.write("h264-ufSSIM,h264-ufPSNR,h264-sfSSIM,h264-sfPSNR,h264-vfSSIM,h264-vfPSNR,h264-ferSSIM,h264-ferPSNR,h264-fSSIM,h265-fPSNR,h264-mSSIM,h264-mPSNR\n"
    + str(ufSSIM_size) + "," + str(ufPSNR_size) + "," + str(sfSSIM_size) + "," + str(sfPSNR_size) + "," 
    + str(vfSSIM_size) + "," + str(vfPSNR_size) + "," + str(ferSSIM_size) + "," + str(ferPSNR_size) + ","
    + str(fSSIM_size) + "," + str(fPSNR_size) + "," + str(mSSIM_size) + "," + str(mPSNR_size) + ","
    + str(sSSIM_size) + "," + str(sPSNR_size) + "," + str(serSSIM_size) + "," + str(serPSNR_size) + ","
    + str(vsSSIM_size) + "," + str(vsPSNR_size))

print("Done")