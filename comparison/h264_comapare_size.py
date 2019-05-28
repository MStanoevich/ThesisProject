import os
import glob

# Creates results file
file_results = open("h264_results/results_size.csv", "w+")

# Paths to txt files for analysis
# Change directory path as appropriate for current dataset
original_path = "data/anotated_mock/original/"

ultrafastSSIM_path = "data/anotated_mock/ultrafastSSIM/"
ultrafastPNSR_path = "data/anotated_mock/ultrafastPNSR/"

superfastSSIM_path = "data/anotated_mock/superfastSSIM/"
superfastPNSR_path = "data/anotated_mock/superfastPNSR/"

veryfastSSIM_path = "data/anotated_mock/veryfastSSIM/"
veryfastPNSR_path = "data/anotated_mock/veryfastPNSR/"

fasterSSIM_path = "data/anotated_mock/fasterSSIM/"
fasterPNSR_path = "data/anotated_mock/fasterPNSR/"

fastSSIM_path = "data/anotated_mock/fastSSIM/"
fastPNSR_path = "data/anotated_mock/fastPNSR/"

mediumSSIM_path = "data/anotated_mock/mediumSSIM/"
mediumPNSR_path = "data/anotated_mock/mediumPNSR/"

# Put files in lists
original_files = glob.glob(original_path + "*.png")

ultrafastSSIM_files = glob.glob(ultrafastSSIM_path + "*.png")
ultrafastPNSR_files = glob.glob(ultrafastPNSR_path + "*.png")

superfastSSIM_files = glob.glob(superfastSSIM_path + "*.png")
superfastPNSR_files = glob.glob(superfastPNSR_path + "*.png")

veryfastSSIM_files = glob.glob(veryfastSSIM_path + "*.png")
veryfastPNSR_files = glob.glob(veryfastPNSR_path + "*.png")

fasterSSIM_files = glob.glob(fasterSSIM_path + "*.png")
fasterPNSR_files = glob.glob(fasterPNSR_path + "*.png")

fastSSIM_files = glob.glob(fastSSIM_path + "*.png")
fastPNSR_files = glob.glob(fastPNSR_path + "*.png")

mediumSSIM_files = glob.glob(mediumSSIM_path + "*.png")
mediumPNSR_files = glob.glob(mediumPNSR_path + "*.png")

total_original = 0
total_ufSSIM = 0
total_ufPNSR = 0
total_sfSSIM = 0
total_sfPNSR = 0
total_vfSSIM = 0
total_vfPNSR = 0
total_ferSSIM = 0
total_ferPNSR = 0
total_fSSIM = 0
total_fPNSR = 0
total_mSSIM = 0
total_mPNSR = 0

for file in original_files:
    total_original += os.stat(file).st_size

for file in ultrafastSSIM_files:
    total_ufSSIM += os.stat(file).st_size

for file in ultrafastPNSR_files:
    total_ufPNSR += os.stat(file).st_size

for file in superfastSSIM_files:
    total_sfSSIM += os.stat(file).st_size

for file in superfastPNSR_files:
    total_sfPNSR += os.stat(file).st_size

for file in veryfastSSIM_files:
    total_vfSSIM += os.stat(file).st_size

for file in veryfastPNSR_files:
    total_vfPNSR += os.stat(file).st_size

for file in fasterSSIM_files:
    total_ferSSIM += os.stat(file).st_size

for file in fasterPNSR_files:
    total_ferPNSR += os.stat(file).st_size

for file in fastSSIM_files:
    total_fSSIM += os.stat(file).st_size

for file in fastPNSR_files:
    total_fPNSR += os.stat(file).st_size

for file in mediumSSIM_files:
    total_mSSIM += os.stat(file).st_size

for file in mediumPNSR_files:
    total_mPNSR += os.stat(file).st_size

file_results.write(str(total_original) + "," + str(total_ufSSIM) + "," + str(total_ufPNSR) + "," 
    + str(total_sfSSIM) + "," + str(total_sfPNSR) + "," + str(total_vfSSIM) + "," + str(total_vfPNSR) + ","
    + str(total_ferSSIM) + "," + str(total_ferPNSR) + "," + str(total_fSSIM) + "," + str(total_fPNSR) + ","
    + str(total_mSSIM) + "," + str(total_mPNSR))   