import csv
from random import randint
import json

suite_test_id = str(randint(100001, 999999))


# def generate_test_file(test_id):
#
#     with open('tests/output_testfiles/bde.csv', 'w', newline='') as csvfile:
#         fieldnames = ['effective_date', 'account_id', 'meter_id', 'endpoint_id']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerow({'effective_date': '2020-01-23','account_id': 'A' + test_id, 'meter_id': 'M' + test_id})
#         writer.writerow({'meter_id': 'M987' + test_id})
#         writer.writerow({'effective_date': '2020-07-01', 'endpoint_id': 'E' + test_id})


def row_accessor(row, test_id):
    new_data_dic = make_new_data_dic()
    if new_data_dic != '':
        new_data_dic = json.loads(new_data_dic)
        print(row)
        for header in row:
            if header in new_data_dic:
                row[header] = new_data_dic[header]
        print(row)


def make_new_data_dic():
    dic = input(str('Enter your values in dictioanry form {"header" : "value", ...} or hit enter to skip to the next row: '))
    return dic

# this version of the converter does not generate python code, it uses console inputs instead
def convert_test_file1(input_file, output_file):

    with open(input_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # print(reader.fieldnames)
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                print(row)
                row_accessor(row,'123')
                writer.writerow(row)


# this version of the converter generates python code for a csv file
def convert_test_file2(input_file, output_file,  mode):

    with open(input_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # this is where the writing part into the .py file begins
        fname = 'code_to generate_translated_DE_files_csv.py'
        line1 = 'import csv'
        line2 = "\n\nwith open('" + output_file +"', 'w', newline='') as csvfile:\n"
        line3 = "\tfieldnames = " + str(reader.fieldnames) + "\n"
        line4 = "\twriter = csv.DictWriter(csvfile, fieldnames=fieldnames)\n"
        line5 = "\twriter.writeheader()\n"

        with open(fname, mode) as f:
            if mode == 'w':
                f.write(line1.format(line1))
            f.write(line2.format(line2))
            f.write(line3.format(line3))
            f.write(line4.format(line4))
            f.write(line5.format(line5))
            for row in reader:
                f.write("\twriter.writerow("+str(row)+")\n")


#### Traversing files and subdirs in a directory as a tree####
# # this is one way to traverse files in a directory using glob + absolute path
# import glob
#
# path = 'C:\\Users\\saldarrs\\Documents\\CVSTranslator_inPython for DE files project\\GenerateCSVfile\\'   # path to project
#
# files = [f for f in glob.glob(path + "**/*.csv", recursive=True)]
#
# for f in files:
#     print(f)
#
# # this is another way to traverse files in a directory using os.walk() + absolute or relative paths
# import os
#
# files = []
# # r=root, d=directories, f = files
# for r, d, f in os.walk("."):    # os.walk(arg) arg could be the absolute path to the directory you want or "." for the relative path of the project
#     for file in f:
#         if '.csv' in file:
#             files.append(os.path.join(r, file))
#
# for f in files:
#     print(f)
#### End of traversing files and subdirs in a dir ####


# #### Traversing a directory for its contents using absolute or relative paths ####
# # 1st method, import the os module, for the os.walk function
# import os
#
# # Set the directory you want to start from
# rootDir_relative = './tests/test_input'
# rootDir_absolute = '/Users/Javier/Documents/BadgerMeter/projects/DEconverter4SQA/tests/test_input'
#
# for dirName, subdirList, fileList in os.walk(rootDir_relative):    # os.walk(path) returns a triple (dirname,
#                                                                     # subdirList, fileList) Now, subdirList is a list of
#                                                                     # all dirs inside that path and fileList is a list
#                                                                     # of all files inside that path including the ones
#                                                                     # inside dirs inside that path
#     print('Found file: %s' % fileList)
# #     for fname in fileList:
# #         print('\t%s' % fname)
# print("--------")
# for dirName, subdirList, fileList in os.walk(rootDir_absolute):    # os.walk(path) returns a triple (dirname, subdirList, fileList)
#     print('Found file: %s' % fileList)
#
# # 2nd method, using glob
# import glob
#
# # Print png images in folder C:\Users\admin\
# for filepath in glob.iglob(r'C:\Users\admin\*.png'):
#     print(filepath)
#
# # Print pdf files in folder C:\Users\admin\
# for filepath in glob.iglob(r'C:\Users\admin\*.pdf'):
#     print(filepath)
# #### End of traversing dirs ####


# this method traverses the input_dir (path of the directory to traverse) and calls the converter on every single csv
# file in it, and then it uses the output_dir (path to the output directory) to define where the output csv files
# will be put after the python file generated is run
# make sure the input_dir and the output_dir exist
def de2py(input_dir, output_dir):
    import os
    dir_path = './' + input_dir
    mode = 'w'
    for filename in os.listdir(dir_path): # os.listdir(path) returns a list of all contents in path (files and dirs)
        if '.csv' in filename:
            convert_test_file2(input_dir + '/' + filename, output_dir + '/d2p_' + filename, mode)
            mode = 'a'


# example call of the de2py method
de2py('tests/test_input', 'tests/output_testfiles')