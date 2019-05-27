import matplotlib.pyplot as plt
import csv

#h264
k_ufSSIM = 0
k_ufPNSR = 0

k_sfSSIM = 0
k_sfPNSR = 0

k_vfSSIM = 0
k_vfPNSR = 0

k_ferSSIM = 0
k_ferPNSR = 0

k_fSSIM = 0
k_fPNSR = 0

k_mSSIM = 0
k_mPNSR = 0

with open("extracted_metrics_for_plotting.csv") as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        k_ufSSIM = float(row[0])
        k_ufPNSR = float(row[1])
        k_sfSSIM = float(row[2])
        k_sfPNSR = float(row[3])
        k_vfSSIM = float(row[4])
        k_vfPNSR = float(row[5])
        k_ferSSIM = float(row[6])
        k_ferPNSR = float(row[7])
        k_fSSIM = float(row[8])
        k_fPNSR = float(row[9])
        k_mSSIM = float(row[10])
        k_mPNSR = float(row[11])

k = [k_ufSSIM, k_ufPNSR, k_sfSSIM, k_sfPNSR, k_vfSSIM, k_vfPNSR, k_ferSSIM, k_ferPNSR, k_fSSIM, k_fPNSR, k_mSSIM, k_mPNSR]
codec = ["ultrafast SSIM", "ultrafast PNSR", "superfast SSIM", "superfast PNSR", "veryfast SSIM", "veryfast PNSR", "faster SSIM", "faster PNSR", "fast SSIM", "fast PNSR", "medium SSIM", "medium PNSR"]
#baseline = [1,1,1]

plt.plot(codec, k)
#plt.plot(codec, baseline)
plt.xlabel('h264 preset & tune')
plt.ylabel('K metric')
plt.show()