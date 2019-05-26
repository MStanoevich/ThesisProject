# Extract metrics out of results
import csv

def percentage(a, b):
    return round(a / b * 100, 2)

total_original_confidence = 0
total_ufSSIM_confidence = 0
total_ufPNSR_confidence = 0
total_mSSIM_confidence = 0

with open("results_confidence.csv") as f:
    for row in csv.reader(f):
        total_original_confidence += int(row[1])
        total_ufSSIM_confidence += int(row[2])
        total_ufPNSR_confidence += int(row[3])
        total_mSSIM_confidence += int(row[4])

total_original_size = 0
total_ufSSIM_size = 0
total_ufPNSR_size = 0
total_mSSIM_size = 0

with open("results_size.csv") as f:
        for row in csv.reader(f):
            total_original_size += int(row[0])
            total_ufSSIM_size += int(row[1])
            total_ufPNSR_size += int(row[2])
            total_mSSIM_size += int(row[3])

# Metrics
ufSSIM_confidence = percentage(total_ufSSIM_confidence, total_original_confidence)
ufSSIM_size = percentage(total_ufSSIM_size, total_original_size)

ufPNSR_confidence = percentage(total_ufPNSR_confidence, total_original_confidence)
ufPNSR_size = percentage(total_ufPNSR_size, total_original_size)

mSSIM_confidence = percentage(total_mSSIM_confidence, total_original_confidence)
mSSIM_size = percentage(total_mSSIM_size, total_original_size)

extracted_metrics = open("extracted_metrics.csv", "w+")
extracted_metrics.write("codec, NN performance compared to original, File size when compared to original, K metric\n"
    + "h264-ultrafastSSIM," + str(ufSSIM_confidence) + "," + str(ufSSIM_size) + "," + str(round(ufSSIM_confidence/ufSSIM_size,2)) + "\n"
    + "h264-ultrafastPNSR," + str(ufPNSR_confidence) + "," + str(ufPNSR_size) + "," + str(round(ufPNSR_confidence/ufPNSR_size,2)) + "\n"
        + "h264-mediumSSIM," + str(mSSIM_confidence) + "," + str(mSSIM_size) + "," + str(round(mSSIM_confidence/mSSIM_size,2)))