import os
import glob

# Creates results file
file_results = open("h264_results/results_size.csv", "w+")

# Paths to txt files for analysis
# Change directory path as appropriate for current dataset
original_path = "data/anotated/original_from_video/"

ultrafastSSIM_path = "data/anotated/ufSSIM/"
ultrafastPSNR_path = "data/anotated/ufPSNR/"

superfastSSIM_path = "data/anotated/sfSSIM/"
superfastPSNR_path = "data/anotated/sfPSNR/"

veryfastSSIM_path = "data/anotated/vfSSIM/"
veryfastPSNR_path = "data/anotated/vfPSNR/"

fasterSSIM_path = "data/anotated/ferSSIM/"
fasterPSNR_path = "data/anotated/ferPSNR/"

fastSSIM_path = "data/anotated/fSSIM/"
fastPSNR_path = "data/anotated/fPSNR/"

mediumSSIM_path = "data/anotated/mSSIM/"
mediumPSNR_path = "data/anotated/mPSNR/"

slowSSIM_path = "data/anotated/sSSIM/"
slowPSNR_path = "data/anotated/sPSNR/"

slowerSSIM_path = "data/anotated/serSSIM/"
slowerPSNR_path = "data/anotated/serPSNR/"

veryslowSSIM_path = "data/anotated/vsSSIM/"
veryslowPSNR_path = "data/anotated/vsPSNR/"

# Put files in lists
original_files = glob.glob(original_path + "*.png")

ultrafastSSIM_files = glob.glob(ultrafastSSIM_path + "*.png")
ultrafastPSNR_files = glob.glob(ultrafastPSNR_path + "*.png")

superfastSSIM_files = glob.glob(superfastSSIM_path + "*.png")
superfastPSNR_files = glob.glob(superfastPSNR_path + "*.png")

veryfastSSIM_files = glob.glob(veryfastSSIM_path + "*.png")
veryfastPSNR_files = glob.glob(veryfastPSNR_path + "*.png")

fasterSSIM_files = glob.glob(fasterSSIM_path + "*.png")
fasterPSNR_files = glob.glob(fasterPSNR_path + "*.png")

fastSSIM_files = glob.glob(fastSSIM_path + "*.png")
fastPSNR_files = glob.glob(fastPSNR_path + "*.png")

mediumSSIM_files = glob.glob(mediumSSIM_path + "*.png")
mediumPSNR_files = glob.glob(mediumPSNR_path + "*.png")

slowSSIM_files = glob.glob(slowSSIM_path + "*.png")
slowPSNR_files = glob.glob(slowPSNR_path + "*.png")

slowerSSIM_files = glob.glob(slowerSSIM_path + "*.png")
slowerPSNR_files = glob.glob(slowerPSNR_path + "*.png")

veryslowSSIM_files = glob.glob(veryslowSSIM_path + "*.png")
veryslowPSNR_files = glob.glob(veryslowPSNR_path + "*.png")

total_original = 0
total_ufSSIM = 0
total_ufPSNR = 0
total_sfSSIM = 0
total_sfPSNR = 0
total_vfSSIM = 0
total_vfPSNR = 0
total_ferSSIM = 0
total_ferPSNR = 0
total_fSSIM = 0
total_fPSNR = 0
total_mSSIM = 0
total_mPSNR = 0
total_sSSIM = 0
total_sPSNR = 0
total_serSSIM = 0
total_serPSNR = 0
total_vsSSIM = 0
total_vsPSNR = 0

for file in original_files:
    total_original += os.stat(file).st_size

for file in ultrafastSSIM_files:
    total_ufSSIM += os.stat(file).st_size

for file in ultrafastPSNR_files:
    total_ufPSNR += os.stat(file).st_size

for file in superfastSSIM_files:
    total_sfSSIM += os.stat(file).st_size

for file in superfastPSNR_files:
    total_sfPSNR += os.stat(file).st_size

for file in veryfastSSIM_files:
    total_vfSSIM += os.stat(file).st_size

for file in veryfastPSNR_files:
    total_vfPSNR += os.stat(file).st_size

for file in fasterSSIM_files:
    total_ferSSIM += os.stat(file).st_size

for file in fasterPSNR_files:
    total_ferPSNR += os.stat(file).st_size

for file in fastSSIM_files:
    total_fSSIM += os.stat(file).st_size

for file in fastPSNR_files:
    total_fPSNR += os.stat(file).st_size

for file in mediumSSIM_files:
    total_mSSIM += os.stat(file).st_size

for file in mediumPSNR_files:
    total_mPSNR += os.stat(file).st_size

for file in slowSSIM_files:
    total_sSSIM += os.stat(file).st_size

for file in slowPSNR_files:
    total_sPSNR += os.stat(file).st_size

for file in slowerSSIM_files:
    total_serSSIM += os.stat(file).st_size

for file in slowerPSNR_files:
    total_serPSNR += os.stat(file).st_size

for file in veryslowSSIM_files:
    total_vsSSIM += os.stat(file).st_size

for file in veryslowPSNR_files:
    total_vsPSNR += os.stat(file).st_size

file_results.write(str(total_original) + "," + str(total_ufSSIM) + "," + str(total_ufPSNR) + "," 
    + str(total_sfSSIM) + "," + str(total_sfPSNR) + "," + str(total_vfSSIM) + "," + str(total_vfPSNR) + ","
    + str(total_ferSSIM) + "," + str(total_ferPSNR) + "," + str(total_fSSIM) + "," + str(total_fPSNR) + ","
    + str(total_mSSIM) + "," + str(total_mPSNR) + "," + str(total_sSSIM) + "," + str(total_sPSNR) + ","
    + str(total_serSSIM) + "," + str(total_serPSNR) + "," + str(total_vsSSIM) + "," + str(total_vsPSNR) + ",")

print("Done") 
