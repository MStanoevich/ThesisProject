#IMPORTANT Where the values for the same preset are the same plot them as one in order to save space on the chart

import matplotlib.pyplot as plt
import csv
import numpy as np

with open("h264_results/combined_confidence_metrics_for_plotting.csv") as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        ufSSIM_conf = float(row[0])
        ufPSNR_conf = float(row[1])
        sfSSIM_conf = float(row[2])
        sfPSNR_conf = float(row[3])
        vfSSIM_conf = float(row[4])
        vfPSNR_conf = float(row[5])
        ferSSIM_conf = float(row[6])
        ferPSNR_conf = float(row[7])
        fSSIM_conf = float(row[8])
        fPSNR_conf = float(row[9])
        mSSIM_conf = float(row[10])
        mPSNR_conf = float(row[11])
        sSSIM_conf = float(row[12])
        sPSNR_conf = float(row[13])
        serSSIM_conf = float(row[14])
        serPSNR_conf = float(row[15])
        vsSSIM_conf = float(row[16])
        vsPSNR_conf = float(row[17])       

with open("h264_results/combined_size_metrics_for_plotting.csv") as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        ufSSIM_size = float(row[0])
        ufPSNR_size = float(row[1])
        sfSSIM_size = float(row[2])
        sfPSNR_size = float(row[3])
        vfSSIM_size = float(row[4])
        vfPSNR_size = float(row[5])
        ferSSIM_size = float(row[6])
        ferPSNR_size = float(row[7])
        fSSIM_size = float(row[8])
        fPSNR_size = float(row[9])
        mSSIM_size = float(row[10])
        mPSNR_size = float(row[11])
        sSSIM_size = float(row[12])
        sPSNR_size = float(row[13])
        serSSIM_size = float(row[14])
        serPSNR_size = float(row[15])
        vsSSIM_size = float(row[16])
        vsPSNR_size = float(row[17])

confidence = [ufSSIM_conf, ufPSNR_conf, sfSSIM_conf, sfPSNR_conf, vfSSIM_conf, vfPSNR_conf, ferSSIM_conf, ferPSNR_conf, fSSIM_conf, fPSNR_conf, mSSIM_conf, mPSNR_conf, sSSIM_conf, sPSNR_conf, serSSIM_conf, serPSNR_conf, vsSSIM_conf, vsSSIM_conf]
size = [ufSSIM_size, ufPSNR_size, sfSSIM_size, sfPSNR_size, vfSSIM_size, vfPSNR_size, ferSSIM_size, ferPSNR_size, fSSIM_size, fPSNR_size, mSSIM_size, mPSNR_size, sSSIM_size, sPSNR_size, serSSIM_size, serPSNR_size, vsSSIM_size, vsPSNR_size]
codec = ["ultrafast SSIM", "ultrafast PSNR", "superfast SSIM", "superfast PSNR", "veryfast SSIM", "veryfast PSNR", "faster SSIM", "faster PSNR", "fast SSIM", "fast PSNR", "medium SSIM", "medium PSNR", "slow SSIM", "slow PSNR", "slower SSIM", "slower PSNR", "veryslow SSIM", "veryslow PSNR"]
ref = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ,17, 18]

# Annotated 2d plot
# plt.grid(True)
# plt.scatter(confidence, size, edgecolors='white')
# plt.xlabel("performance %")
# plt.ylabel("size %")
# plt.axhline(100, lw = 0.5, color = 'black')
# plt.axvline(100, lw = 0.5, color = 'black')
# plt.title('Annotated dataset')
# plt.grid(True)

# for i, txt in enumerate(ref):
#     if i == 8:
#         plt.annotate(txt, (confidence[i] + 0.03, size[i] - 0.3))
#     elif i == 13:
#         plt.annotate(txt, (confidence[i] + 0.03, size[i] - 0.1))
#     else:
#         plt.annotate(txt, (confidence[i] + 0.03, size[i] + 0.03))

# Non Annotated dataset
# plt.grid(True)
# plt.scatter(confidence, size, edgecolors='white')
# plt.xlabel("performance %")
# plt.ylabel("size %")
# plt.axhline(100, lw = 0.5, color = 'black')
# plt.axvline(100, lw = 0.5, color = 'black')
# plt.title('Non annotated dataset')
# plt.grid(True)

# for i, txt in enumerate(ref):
#     if i == 12:
#         plt.annotate(txt, (confidence[i] + 0.1, size[i] - 0.4))
#     elif i == 13:
#         plt.annotate(txt, (confidence[i] + 0.1, size[i] - 0.2))
#     elif i == 14:
#         plt.annotate(txt, (confidence[i] + 0.1, size[i] - 0.4))
#     elif i == 16:
#         plt.annotate(txt, (confidence[i] - 0.55, size[i] + 0.1))
#     else:
#         plt.annotate(txt, (confidence[i] + 0.1, size[i] + 0.1))

# Combined 2d plot
plt.scatter(confidence, size, edgecolors='white')
plt.xlabel("performance %")
plt.ylabel("size %")
plt.axhline(100, lw = 0.5, color = 'black')
plt.axvline(100, lw = 0.5, color = 'black')
plt.grid(True)
plt.title('Average results from both datasets')

for i, txt in enumerate(ref):
    if i == 14:
        plt.annotate(txt, (confidence[i] - 0.35, size[i] - 0.05))
    elif i == 16:
        plt.annotate(txt, (confidence[i] + 0.03, size[i] - 0.05))
    else:
        plt.annotate(txt, (confidence[i] + 0.03, size[i] + 0.03))

plt.show()