import matplotlib.pyplot as plt
import csv

#h264
k_ufSSIM = 0
k_ufPNSR = 0
k_mSSIM = 0

with open("extracted_metrics_for_plotting.csv") as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        k_ufSSIM = float(row[0])
        k_ufPNSR = float(row[1])
        k_mSSIM = float(row[2])

k = [k_ufSSIM, k_ufPNSR, k_mSSIM]
codec = ["ultrafast SSIM", "ultrafast PNSR", "medium SSIM"]
baseline = [1,1,1]

plt.plot(codec, k)
plt.plot(codec, baseline)
plt.xlabel('preset & tune')
plt.ylabel('K metric')
plt.show()