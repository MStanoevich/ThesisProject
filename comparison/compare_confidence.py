import glob
import re

# Creates results file
file_results = open("results_confidence.csv", "w+")

# Paths to txt files for analysis
original_anotated_path = "data_results/anotated_results/"
original_non_anotated_path = "data_results/non_anotated_results/"

ultrafastSSIM_anotated_results_path = "data_results/ultrafastSSIM_results/anotated_results/"
ultrafastPNSR_anotated_results_path = "data_results/ultrafastPNSR_results/anotated_results/"

mediumSSIM_anotated_results_path = "data_results/mediumSSIM_results/anotated_results/"

# Open files, put them in lists and sort those lists by name
dre = re.compile(r'(\d+)')

files = glob.glob(original_anotated_path + "*.txt")
files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

ultrafastSSIM_files = glob.glob(ultrafastSSIM_anotated_results_path + "*.txt")
ultrafastSSIM_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

ultrafastPNSR_files = glob.glob(ultrafastPNSR_anotated_results_path + "*.txt")
ultrafastPNSR_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

mediumSSIM_files = glob.glob(mediumSSIM_anotated_results_path + "*.txt")
mediumSSIM_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

# Calcuates totals and writes them to results file
for file_original, file_ufSSIM, file_ufPNSR, file_mSSIM in zip(files, ultrafastSSIM_files, ultrafastPNSR_files, mediumSSIM_files):
    
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

    # ultrafastPNSR
    result_ufPNSR = open(file_ufPNSR)
    print(result_ufPNSR.name)
    total_ufPNSR = 0
    list_ufPNSR = list()

    for line in result_ufPNSR:
        confidence = re.findall('[0-9]+', line)
        list_ufPNSR += confidence
        print(line)
    
    for i in list_ufPNSR:
        total_ufPNSR += int(i)

    print(total_ufPNSR)

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

    result_original_name = re.findall('[0-9]+', result_original.name)
    file_results.writelines(str(result_original_name) + "," + str(total_original) + "," + str(total_ufSSIM) + "," + str(total_ufPNSR) + "," + str(total_mSSIM) + "\n")