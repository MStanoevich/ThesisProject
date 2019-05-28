import glob
import re

# Creates results file
file_results = open("h264_results/results_confidence.csv", "w+")

# Paths to txt files for analysis
# Change directory paths as appropriate for current dataset
original_path = "data_results/anotated/original_from_video/"

ultrafastSSIM_results_path = "data_results/anotated/ultrafast-ssim/"
ultrafastPSNR_results_path = "data_results/anotated/ultrafast-psnr/"

superfastSSIM_results_path = "data_results/anotated/superfast-ssim/"
superfastPSNR_results_path = "data_results/anotated/superfast-psnr/"

veryfastSSIM_results_path = "data_results/anotated/veryfast-ssim/"
veryfastPSNR_results_path = "data_results/anotated/veryfast-psnr/"

fasterSSIM_results_path = "data_results/anotated/faster-ssim/"
fasterPSNR_results_path = "data_results/anotated/faster-psnr/"

fastSSIM_results_path = "data_results/anotated/fast-ssim/"
fastPSNR_results_path = "data_results/anotated/fast-psnr/"

mediumSSIM_results_path = "data_results/anotated/medium-ssim/"
mediumPSNR_results_path = "data_results/anotated/medium-psnr/"

slowSSIM_results_path = "data_results/anotated/slow-ssim/"
slowPSNR_results_path = "data_results/anotated/slow-psnr/"

slowerSSIM_results_path = "data_results/anotated/slower-ssim/"
slowerPSNR_results_path = "data_results/anotated/slower-psnr/"

veryslowSSIM_results_path = "data_results/anotated/veryslow-ssim/"
veryslowPSNR_results_path = "data_results/anotated/veryslow-psnr/"

# Open files, put them in lists and sort those lists by name
dre = re.compile(r'(\d+)')

original_files = glob.glob(original_path + "*.txt")
original_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

ultrafastSSIM_files = glob.glob(ultrafastSSIM_results_path + "*.txt")
ultrafastSSIM_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

ultrafastPSNR_files = glob.glob(ultrafastPSNR_results_path + "*.txt")
ultrafastPSNR_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

superfastSSIM_files = glob.glob(superfastSSIM_results_path + "*.txt")
superfastSSIM_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

superfastPSNR_files = glob.glob(superfastPSNR_results_path + "*.txt")
superfastPSNR_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

veryfastSSIM_files = glob.glob(veryfastSSIM_results_path + "*.txt")
veryfastSSIM_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

veryfastPSNR_files = glob.glob(veryfastPSNR_results_path + "*.txt")
veryfastPSNR_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

fasterSSIM_files = glob.glob(fasterSSIM_results_path + "*.txt")
fasterSSIM_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

fasterPSNR_files = glob.glob(fasterPSNR_results_path + "*.txt")
fasterPSNR_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

fastSSIM_files = glob.glob(fastSSIM_results_path + "*.txt")
fastSSIM_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

fastPSNR_files = glob.glob(fastPSNR_results_path + "*.txt")
fastPSNR_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

mediumSSIM_files = glob.glob(mediumSSIM_results_path + "*.txt")
mediumSSIM_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

mediumPSNR_files = glob.glob(mediumPSNR_results_path + "*.txt")
mediumPSNR_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

slowSSIM_files = glob.glob(slowSSIM_results_path + "*.txt")
slowSSIM_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

slowPSNR_files = glob.glob(slowPSNR_results_path + "*.txt")
slowPSNR_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

slowerSSIM_files = glob.glob(slowerSSIM_results_path + "*.txt")
slowerSSIM_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

slowerPSNR_files = glob.glob(slowerPSNR_results_path + "*.txt")
slowerPSNR_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

veryslowSSIM_files = glob.glob(veryslowSSIM_results_path + "*.txt")
veryslowSSIM_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

veryslowPSNR_files = glob.glob(veryslowPSNR_results_path + "*.txt")
veryslowPSNR_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

# Calcuates totals and writes them to results file
for file_original, file_ufSSIM, file_ufPSNR, file_sfSSIM, file_sfPSNR, file_vfSSIM, file_vfPSNR, file_ferSSIM, file_ferPSNR, file_fSSIM, file_fPSNR, file_mSSIM, file_mPSNR, file_sSSIM, file_sPSNR, file_serSSIM, file_serPSNR, file_vsSSIM, file_vsPSNR in zip(original_files, ultrafastSSIM_files, ultrafastPSNR_files, superfastSSIM_files, superfastPSNR_files, veryfastSSIM_files, veryfastPSNR_files, fasterSSIM_files, fasterPSNR_files, fastSSIM_files, fastPSNR_files, mediumSSIM_files, mediumPSNR_files, slowSSIM_files, slowPSNR_files, slowerSSIM_files, slowerPSNR_files, veryslowSSIM_files, veryslowPSNR_files):
    
    # original
    result_original = open(file_original)
    print(result_original.name)
    total_original = 0
    list_original = list()
    
    for line in result_original:
        confidence = re.findall('[0-9]+',line)
        list_original += confidence
        print(line)

    for i in list_original:
        total_original += int(i)
    
    print(total_original)

    # ultraSSIM
    result_ufSSIM = open(file_ufSSIM)
    print(result_ufSSIM.name)
    total_ufSSIM = 0
    list_ufSSIM = list()

    for line in result_ufSSIM:
        confidence = re.findall('[0-9]+', line)
        list_ufSSIM += confidence
        print(line)
    
    for i in list_ufSSIM:
        total_ufSSIM += int(i)

    print(total_ufSSIM)

    # ultrafastPSNR
    result_ufPSNR = open(file_ufPSNR)
    print(result_ufPSNR.name)
    total_ufPSNR = 0
    list_ufPSNR = list()

    for line in result_ufPSNR:
        confidence = re.findall('[0-9]+', line)
        list_ufPSNR += confidence
        print(line)
    
    for i in list_ufPSNR:
        total_ufPSNR += int(i)

    print(total_ufPSNR)

    # superfastSSIM
    result_sfSSIM = open(file_sfSSIM)
    print(result_sfSSIM.name)
    total_sfSSIM = 0
    list_sfSSIM = list()

    for line in result_sfSSIM:
        confidence = re.findall('[0-9]+', line)
        list_sfSSIM += confidence
        print(line)
    
    for i in list_sfSSIM:
        total_sfSSIM += int(i)

    print(total_sfSSIM)

    # superfastSSIM
    result_sfPSNR = open(file_sfPSNR)
    print(result_sfPSNR.name)
    total_sfPSNR = 0
    list_sfPSNR = list()

    for line in result_sfPSNR:
        confidence = re.findall('[0-9]+', line)
        list_sfPSNR += confidence
        print(line)

    for i in list_sfPSNR:
        total_sfPSNR += int(i)

    print(total_sfPSNR)

    # veryfastSSIM
    result_vfSSIM = open(file_vfSSIM)
    print(result_vfSSIM.name)
    total_vfSSIM = 0
    list_vfSSIM = list()

    for line in result_vfSSIM:
        confidence = re.findall('[0-9]+', line)
        list_vfSSIM += confidence
        print(line)

    for i in list_vfSSIM:
        total_vfSSIM += int(i)

    print(total_vfSSIM)

    # veryfastPSNR
    result_vfPSNR = open(file_vfPSNR)
    print(result_vfPSNR.name)
    total_vfPSNR = 0
    list_vfPSNR = list()

    for line in result_vfPSNR:
        confidence = re.findall('[0-9]+', line)
        list_vfPSNR += confidence
        print(line)

    for i in list_vfPSNR:
        total_vfPSNR += int(i)

    print(total_vfPSNR)

    # fasterSSIM
    result_ferSSIM = open(file_ferSSIM)
    print(result_ferSSIM.name)
    total_ferSSIM = 0
    list_ferSSIM = list()

    for line in result_ferSSIM:
        confidence = re.findall('[0-9]+', line)
        list_ferSSIM += confidence
        print(line)
    
    for i in list_ferSSIM:
        total_ferSSIM += int(i)

    print(total_ferSSIM)

    # fasterPSNR
    result_ferPSNR = open(file_ferPSNR)
    print(result_ferPSNR.name)
    total_ferPSNR = 0
    list_ferPSNR = list()

    for line in result_ferPSNR:
        confidence = re.findall('[0-9]+', line)
        list_ferPSNR += confidence
        print(line)
    
    for i in list_ferPSNR:
        total_ferPSNR += int(i)

    print(total_ferPSNR)

    # fastSSIM
    result_fSSIM = open(file_fSSIM)
    print(result_fSSIM.name)
    total_fSSIM = 0
    list_fSSIM = list()

    for line in result_fSSIM:
        confidence = re.findall('[0-9]+', line)
        list_fSSIM += confidence
        print(line)
    
    for i in list_fSSIM:
        total_fSSIM += int(i)

    print(total_fSSIM)

    # fastPSNR
    result_fPSNR = open(file_fPSNR)
    print(result_fPSNR.name)
    total_fPSNR = 0
    list_fPSNR = list()

    for line in result_fPSNR:
        confidence = re.findall('[0-9]+', line)
        list_fPSNR += confidence
        print(line)
    
    for i in list_fPSNR:
        total_fPSNR += int(i)

    print(total_fPSNR)

    # mediumSSIM
    result_mSSIM = open(file_mSSIM)
    print(result_mSSIM.name)
    total_mSSIM = 0
    list_mSSIM = list()

    for line in result_mSSIM:
        confidence = re.findall('[0-9]+', line)
        list_mSSIM += confidence
        print(line)
    
    for i in list_mSSIM:
        total_mSSIM += int(i)

    print(total_mSSIM)

    # mediumPSNR
    result_mPSNR = open(file_mPSNR)
    print(result_mPSNR)
    total_mPSNR = 0
    list_mPSNR = list()

    for line in result_mPSNR:
        confidence = re.findall('[0-9]+', line)
        list_mPSNR += confidence
        print(line)
    
    for i in list_mPSNR:
        total_mPSNR += int(i)

    print(total_mPSNR)

    # TODO add vsSSIM, vsPSNR

    # slowSSIM
    result_sSSIM = open(file_sSSIM)
    print(result_sSSIM.name)
    total_sSSIM = 0
    list_sSSIM = list()

    for line in result_sSSIM:
        confidence = re.findall('[0-9]+', line)
        list_sSSIM += confidence
        print(line)
    
    for i in list_sSSIM:
        total_sSSIM += int(i)

    print(total_sSSIM)

    # slowPSNR
    result_sPSNR = open(file_sPSNR)
    print(result_sPSNR)
    total_sPSNR = 0
    list_sPSNR = list()

    for line in result_sPSNR:
        confidence = re.findall('[0-9]+', line)
        list_sPSNR += confidence
        print(line)
    
    for i in list_sPSNR:
        total_sPSNR += int(i)

    print(total_sPSNR)

    # slowerSSIM
    result_serSSIM = open(file_serSSIM)
    print(result_serSSIM.name)
    total_serSSIM = 0
    list_serSSIM = list()

    for line in result_serSSIM:
        confidence = re.findall('[0-9]+', line)
        list_serSSIM += confidence
        print(line)
    
    for i in list_serSSIM:
        total_serSSIM += int(i)

    print(total_serSSIM)

    # slowerPSNR
    result_serPSNR = open(file_serPSNR)
    print(result_serPSNR)
    total_serPSNR = 0
    list_serPSNR = list()

    for line in result_serPSNR:
        confidence = re.findall('[0-9]+', line)
        list_serPSNR += confidence
        print(line)
    
    for i in list_serPSNR:
        total_serPSNR += int(i)

    print(total_serPSNR)

    # veryslowSSIM
    result_vsSSIM = open(file_vsSSIM)
    print(result_vsSSIM.name)
    total_vsSSIM = 0
    list_vsSSIM = list()

    for line in result_vsSSIM:
        confidence = re.findall('[0-9]+', line)
        list_vsSSIM += confidence
        print(line)
    
    for i in list_vsSSIM:
        total_vsSSIM += int(i)

    print(total_vsSSIM)

    # veryslowPSNR
    result_vsPSNR = open(file_vsPSNR)
    print(result_vsPSNR)
    total_vsPSNR = 0
    list_vsPSNR = list()

    for line in result_vsPSNR:
        confidence = re.findall('[0-9]+', line)
        list_vsPSNR += confidence
        print(line)
    
    for i in list_vsPSNR:
        total_vsPSNR += int(i)

    print(total_vsPSNR)

    # Write data to csv
    result_original_name = re.findall('[0-9]+', result_original.name)
    file_results.writelines(str(result_original_name) + "," + str(total_original) + ","
    + str(total_ufSSIM) + "," + str(total_ufPSNR) + "," + str(total_sfSSIM) + "," + str(total_sfPSNR) + "," 
    + str(total_vfSSIM) + "," + str(total_vfPSNR) + "," + str(total_ferSSIM) + "," + str(total_ferPSNR) + ","
    + str(total_fSSIM) + "," + str(total_fPSNR) + "," + str(total_mSSIM) + "," + str(total_mPSNR) + ","
    + str(total_sSSIM) + "," + str(total_sPSNR) + "," + str(total_serSSIM) + "," + str(total_serPSNR) + ","
    + str(total_vsSSIM) + "," + str(total_vsPSNR) + "\n")