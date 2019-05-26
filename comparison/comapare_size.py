import os
import glob

# Creates results file
file_results = open("results_size.csv", "w+")

# Paths to txt files for analysis
original_anotated_path = "data/original/"

ultrafastSSIM_anotated_path = "data/ultrafastSSIM/"
ultrafastPNSR_anotated_path = "data/ultrafastPNSR/"

mediumSSIM_anotated_path = "data/mediumSSIM/"

# Put files in lists
original_files = glob.glob(original_anotated_path + "*.png")

ultrafastSSIM_files = glob.glob(ultrafastSSIM_anotated_path + "*.png")

ultrafastPNSR_files = glob.glob(ultrafastPNSR_anotated_path + "*.png")

mediumSSIM_files = glob.glob(mediumSSIM_anotated_path + "*.png")

total_original = 0
total_ufSSIM = 0
total_ufPNSR = 0
total_mSSIM = 0

for file in original_files:
    total_original += os.stat(file).st_size

for file in ultrafastSSIM_files:
    total_ufSSIM += os.stat(file).st_size

for file in ultrafastPNSR_files:
    total_ufPNSR += os.stat(file).st_size

for file in mediumSSIM_files:
    total_mSSIM += os.stat(file).st_size

file_results.write(str(total_original) + "," + str(total_ufSSIM) + "," + str(total_ufPNSR) + "," + str(total_mSSIM))   
