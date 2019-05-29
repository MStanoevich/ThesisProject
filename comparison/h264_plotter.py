#IMPORTANT Where the values for the same preset are the same plot them as one in order to save space on the chart

import matplotlib.pyplot as plt
import csv
import numpy as np

#h264
# with open("h264_results/k_metrics_for_plotting.csv") as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     for row in f_csv:
#         k_ufSSIM = float(row[0])
#         k_ufPSNR = float(row[1])
#         k_sfSSIM = float(row[2])
#         k_sfPSNR = float(row[3])
#         k_vfSSIM = float(row[4])
#         k_vfPSNR = float(row[5])
#         k_ferSSIM = float(row[6])
#         k_ferPSNR = float(row[7])
#         k_fSSIM = float(row[8])
#         k_fPSNR = float(row[9])
#         k_mSSIM = float(row[10])
#         k_mPSNR = float(row[11])
#         k_sSSIM = float(row[12])
#         k_sPSNR = float(row[13])
#         k_serSSIM = float(row[14])
#         k_serPSNR = float(row[15])
#         k_vsSSIM = float(row[16])
#         k_vsPSNR = float(row[17])

with open("h264_results/confidence_metrics_for_plotting.csv") as f:
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

# with open("h264_results/size_metrics_for_plotting.csv") as f:
#     f_csv = csv.reader(f)
#     headers = next(f_csv)
#     for row in f_csv:
#         ufSSIM_size = float(row[0])
#         ufPSNR_size = float(row[1])
#         sfSSIM_size = float(row[2])
#         sfPSNR_size = float(row[3])
#         vfSSIM_size = float(row[4])
#         vfPSNR_size = float(row[5])
#         ferSSIM_size = float(row[6])
#         ferPSNR_size = float(row[7])
#         fSSIM_size = float(row[8])
#         fPSNR_size = float(row[9])
#         mSSIM_size = float(row[10])
#         mPSNR_size = float(row[11])
#         sSSIM_size = float(row[12])
#         sPSNR_size = float(row[13])
#         serSSIM_size = float(row[14])
#         serPSNR_size = float(row[15])
#         vsSSIM_size = float(row[16])
#         vsPSNR_size = float(row[17])

#k = [k_ufSSIM, k_ufPSNR, k_sfSSIM, k_sfPSNR, k_vfSSIM, k_vfPSNR, k_ferSSIM, k_ferPSNR, k_fSSIM, k_fPSNR, k_mSSIM, k_mPSNR, k_sSSIM, k_sPSNR, k_serSSIM, k_serPSNR, k_vsSSIM, k_vsPSNR]
confidence = [ufSSIM_conf, ufPSNR_conf, sfSSIM_conf, sfPSNR_conf, vfSSIM_conf, vfPSNR_conf, ferSSIM_conf, ferPSNR_conf, fSSIM_conf, fPSNR_conf, mSSIM_conf, mPSNR_conf, sSSIM_conf, sPSNR_conf, serSSIM_conf, serPSNR_conf, vsSSIM_conf, vsSSIM_conf]
#size = [ufSSIM_size, ufPSNR_size, sfSSIM_size, sfPSNR_size, vfSSIM_size, vfPSNR_size, ferSSIM_size, ferPSNR_size, fSSIM_size, fPSNR_size, mSSIM_size, mPSNR_size, sSSIM_size, sPSNR_size, serSSIM_size, serPSNR_size, vsSSIM_size, vsPSNR_size]
codec = ["ultrafast SSIM", "ultrafast PSNR", "superfast SSIM", "superfast PSNR", "veryfast SSIM", "veryfast PSNR", "faster SSIM", "faster PSNR", "fast SSIM", "fast PSNR", "medium SSIM", "medium PSNR", "slow SSIM", "slow PSNR", "slower SSIM", "slower PSNR", "veryslow SSIM", "veryslow PSNR"]
#baseline = [1,1,1,1,1,1,1,1,1,1,1,1]

# To plot k metric
#plt.plot(codec, k)
#plt.plot(codec, baseline)
#plt.xlabel('h264 preset & tune')
#plt.ylabel('K metric')

# To plot confidence performance
# plt.plot(codec, confidence)
# plt.xlabel('h264 preset & tune')
# plt.ylabel('Performance % compared to original')

# To plot size 
# plt.plot(codec, size)
# plt.xlabel('h264 preset & tune')
# plt.ylabel('File size % compared to original')

# TODO finnish
# To plot barchart performance
index = np.arange(len(codec))
plt.plot(index, confidence)
plt.xlabel('h264 preset & tune')
plt.ylabel('Performance % compared to original')
plt.xticks(index, codec, fontsize=10, rotation=30)
plt.title('Neural network performance on compressed anotated dataset')

plt.show()