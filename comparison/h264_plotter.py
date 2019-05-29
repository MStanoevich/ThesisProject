#IMPORTANT Where the values for the same preset are the same plot them as one in order to save space on the chart

import matplotlib.pyplot as plt
import csv

#h264
# with open("h264_results/k_metrics_for_plotting.csv") as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     for row in f_csv:
#         k_ufSSIM = float(row[0])
#         k_ufPNSR = float(row[1])
#         k_sfSSIM = float(row[2])
#         k_sfPNSR = float(row[3])
#         k_vfSSIM = float(row[4])
#         k_vfPNSR = float(row[5])
#         k_ferSSIM = float(row[6])
#         k_ferPNSR = float(row[7])
#         k_fSSIM = float(row[8])
#         k_fPNSR = float(row[9])
#         k_mSSIM = float(row[10])
#         k_mPNSR = float(row[11])

with open("h264_results/confidence_metrics_for_plotting.csv") as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        ufSSIM_conf = float(row[0])
        ufPNSR_conf = float(row[1])
        sfSSIM_conf = float(row[2])
        sfPNSR_conf = float(row[3])
        vfSSIM_conf = float(row[4])
        vfPNSR_conf = float(row[5])
        ferSSIM_conf = float(row[6])
        ferPNSR_conf = float(row[7])
        fSSIM_conf = float(row[8])
        fPNSR_conf = float(row[9])
        mSSIM_conf = float(row[10])
        mPNSR_conf = float(row[11])

# with open("h264_results/size_metrics_for_plotting.csv") as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     for row in f_csv:
#         ufSSIM_size = float(row[0])
#         ufPNSR_size = float(row[1])
#         sfSSIM_size = float(row[2])
#         sfPNSR_size = float(row[3])
#         vfSSIM_size = float(row[4])
#         vfPNSR_size = float(row[5])
#         ferSSIM_size = float(row[6])
#         ferPNSR_size = float(row[7])
#         fSSIM_size = float(row[8])
#         fPNSR_size = float(row[9])
#         mSSIM_size = float(row[10])
#         mPNSR_size = float(row[11])

#k = [k_ufSSIM, k_ufPNSR, k_sfSSIM, k_sfPNSR, k_vfSSIM, k_vfPNSR, k_ferSSIM, k_ferPNSR, k_fSSIM, k_fPNSR, k_mSSIM, k_mPNSR]
confidence = [ufSSIM_conf, ufPNSR_conf, sfSSIM_conf, sfPNSR_conf, vfSSIM_conf, vfPNSR_conf, ferSSIM_conf, ferPNSR_conf, fSSIM_conf, fPNSR_conf, mSSIM_conf, mPNSR_conf]
#size = [ufSSIM_size, ufPNSR_size, sfSSIM_size, sfPNSR_size, vfSSIM_size, vfPNSR_size, ferSSIM_size, ferPNSR_size, fSSIM_size, fPNSR_size, mSSIM_size, mPNSR_size]
codec = ["ultrafast SSIM", "ultrafast PNSR", "superfast SSIM", "superfast PNSR", "veryfast SSIM", "veryfast PNSR", "faster SSIM", "faster PNSR", "fast SSIM", "fast PNSR", "medium SSIM", "medium PNSR"]
baseline = [1,1,1,1,1,1,1,1,1,1,1,1]

# To plot k metric
#plt.plot(codec, k)
#plt.plot(codec, baseline)
#plt.xlabel('h264 preset & tune')
#plt.ylabel('K metric')

# To plot confidence performance
plt.plot(codec, confidence)
plt.xlabel('h264 preset & tune')
plt.ylabel('Performance % compared to original')

# To plot size 
# plt.plot(codec, size)
# plt.xlabel('h264 preset & tune')
# plt.ylabel('File size % compared to original')

# TODO finnish
# To plot barchart performance
#plt.bart(performance, codec, align = 'center', alpha=0.5)

plt.show()