import glob
import re

# Creates results file
file_results = open("results_confidence.csv", "w+")

# Paths to txt files for analysis
original_anotated_path = "data_results/anotated_results/"
original_non_anotated_path = "data_results/non_anotated_results/"

ultrafastSSIM_anotated_results_path = "data_results/ultrafastSSIM_results/anotated_results/"
ultrafastPNSR_anotated_results_path = "data_results/ultrafastPNSR_results/anotated_results/"

superfastSSIM_anotated_results_path = "data_results/superfastSSIM_results/anotated_results/"
superfastPNSR_anotated_results_path = "data_results/superfastPNSR_results/anotated_results/"

veryfastSSIM_anotated_results_path = "data_results/veryfastSSIM_results/anotated_results/"
veryfastPNSR_anotated_results_path = "data_results/veryfastPNSR_results/anotated_results/"

fasterSSIM_anotated_results_path = "data_results/fasterSSIM_results/anotated_results/"
fasterPNSR_anotated_results_path = "data_results/fasterPNSR_results/anotated_results/"

fastSSIM_anotated_results_path = "data_results/fastSSIM_results/anotated_results/"
fastPNSR_anotated_results_path = "data_results/fastPNSR_results/anotated_results/"

mediumSSIM_anotated_results_path = "data_results/mediumSSIM_results/anotated_results/"
mediumPNSR_anotated_results_path = "data_results/mediumPNSR_results/anotated_results/"

# Open files, put them in lists and sort those lists by name
dre = re.compile(r'(\d+)')

original_anotated_files = glob.glob(original_anotated_path + "*.txt")
original_anotated_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

ultrafastSSIM_files = glob.glob(ultrafastSSIM_anotated_results_path + "*.txt")
ultrafastSSIM_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

ultrafastPNSR_files = glob.glob(ultrafastPNSR_anotated_results_path + "*.txt")
ultrafastPNSR_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

superfastSSIM_files = glob.glob(superfastSSIM_anotated_results_path + "*.txt")
superfastSSIM_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

superfastPNSR_files = glob.glob(superfastPNSR_anotated_results_path + "*.txt")
superfastPNSR_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

veryfastSSIM_files = glob.glob(veryfastSSIM_anotated_results_path + "*.txt")
veryfastSSIM_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

veryfastPNSR_files = glob.glob(veryfastPNSR_anotated_results_path + "*.txt")
veryfastPNSR_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

fasterSSIM_files = glob.glob(fasterSSIM_anotated_results_path + "*.txt")
fasterSSIM_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

fasterPNSR_files = glob.glob(fasterPNSR_anotated_results_path + "*.txt")
fasterPNSR_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

fastSSIM_files = glob.glob(fastSSIM_anotated_results_path + "*.txt")
fastSSIM_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

fastPNSR_files = glob.glob(fastPNSR_anotated_results_path + "*.txt")
fastPNSR_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

mediumSSIM_files = glob.glob(mediumSSIM_anotated_results_path + "*.txt")
mediumSSIM_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

mediumPNSR_files = glob.glob(mediumPNSR_anotated_results_path + "*.txt")
mediumPNSR_files.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in re.split(dre, l)])

# Calcuates totals and writes them to results file
for file_original, file_ufSSIM, file_ufPNSR, file_sfSSIM, file_sfPNSR, file_vfSSIM, file_vfPNSR, file_ferSSIM, file_ferPNSR, file_fSSIM, file_fPNSR, file_mSSIM, file_mPNSR in zip(original_anotated_files, ultrafastSSIM_files, ultrafastPNSR_files, superfastSSIM_files, superfastPNSR_files, veryfastSSIM_files, veryfastPNSR_files, fasterSSIM_files, fasterPNSR_files, fastSSIM_files, fastPNSR_files, mediumSSIM_files, mediumPNSR_files):
    
    # original anotated
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

    # ultraSSIM anotated
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

    # ultrafastPNSR anotated
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

    # superfastSSIM anotated
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

    # superfastSSIM anotated
    result_sfPNSR = open(file_sfPNSR)
    print(result_sfPNSR.name)
    total_sfPNSR = 0
    list_sfPNSR = list()

    for line in result_sfPNSR:
        confidence = re.findall('[0-9]+', line)
        list_sfPNSR += confidence
        print(line)

    for i in list_sfPNSR:
        total_sfPNSR += int(i)

    print(total_sfPNSR)

    # veryfastSSIM anotated
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

    # veryfastPNSR anotated
    result_vfPNSR = open(file_vfPNSR)
    print(result_vfPNSR.name)
    total_vfPNSR = 0
    list_vfPNSR = list()

    for line in result_vfPNSR:
        confidence = re.findall('[0-9]+', line)
        list_vfPNSR += confidence
        print(line)

    for i in list_vfPNSR:
        total_vfPNSR += int(i)

    print(total_vfPNSR)

    # fasterSSIM anotated
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

    # fasterPNSR anotated
    result_ferPNSR = open(file_ferPNSR)
    print(result_ferPNSR.name)
    total_ferPNSR = 0
    list_ferPNSR = list()

    for line in result_ferPNSR:
        confidence = re.findall('[0-9]+', line)
        list_ferPNSR += confidence
        print(line)
    
    for i in list_ferPNSR:
        total_ferPNSR += int(i)

    print(total_ferPNSR)

    # fastSSIM anotated
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

    # fastPNSR anotated
    result_fPNSR = open(file_fPNSR)
    print(result_fPNSR.name)
    total_fPNSR = 0
    list_fPNSR = list()

    for line in result_fPNSR:
        confidence = re.findall('[0-9]+', line)
        list_fPNSR += confidence
        print(line)
    
    for i in list_fPNSR:
        total_fPNSR += int(i)

    print(total_fPNSR)

    # mediumSSIM anotated
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

    # mediumPNSR anotated
    result_mPNSR = open(file_mPNSR)
    print(result_mPNSR)
    total_mPNSR = 0
    list_mPNSR = list()

    for line in result_mPNSR:
        confidence = re.findall('[0-9]+', line)
        list_mPNSR += confidence
        print(line)
    
    for i in list_mPNSR:
        total_mPNSR += int(i)

    print(total_mPNSR)

    # Write anotaed data to csv
    result_original_name = re.findall('[0-9]+', result_original.name)
    file_results.writelines(str(result_original_name) + "," + str(total_original) + "," 
    + str(total_ufSSIM) + "," + str(total_ufPNSR) + "," + str(total_sfSSIM) + "," + str(total_sfPNSR) + "," 
    + str(total_vfSSIM) + "," + str(total_vfPNSR) + "," + str(total_ferSSIM) + "," + str(total_ferPNSR) + ","
    + str(total_fSSIM) + "," + str(total_fPNSR) + "," + str(total_mSSIM) + "," + str(total_mPNSR) + "\n")

#TODO create loop for non_anotated data