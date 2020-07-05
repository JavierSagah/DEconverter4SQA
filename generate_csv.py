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
    # fname = 'code_for_' + input_file.split('.')[0]+ '_csv.py'
    # line1 = 'import csv\n\n'
    # line2 = "with open('"+input_file+"', newline='') as csvfile:\n"
    # line3 = "\treader = csv.DictReader(csvfile)\n"
    # line4 = "\twith open('output_testfiles/translated_bde.csv', 'w', newline='') as csvfile:\n"
    # line5 = "\t\tfieldnames = reader.fieldnames\n\t\twriter = csv.DictWriter(csvfile, fieldnames=fieldnames)\n\t\twriter.writeheader()\n\t\tfor row in reader:\n\t\t\twriter.writerow(row)"
    #
    # with open(fname, 'w') as f:
    #     f.write(line1.format(line1))
    #     f.write(line2.format(line2))
    #     f.write(line3.format(line3))
    #     f.write(line4.format(line4))
    #     f.write(line5.format(line5))

    # import code_for_generating_csv_file
    # print(code_for_generating_csv_file.data)


def convert_test_file2(input_file, output_file,  mode):

    with open(input_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
    #     # print(reader.fieldnames)
    #     with open('tests/output_testfiles/translated_bde.csv', 'w', newline='') as csvfile:
    #         fieldnames = reader.fieldnames
    #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #         writer.writeheader()
    #         for row in reader:
    #             row_accessor(row,'123')
    #             writer.writerow(row)
        fname = 'code_to generate_translated_DE_files_csv.py'# + input_file.split('.')[0]+ '_csv.py'
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


# generate_test_file(suite_test_id)
convert_test_file1('tests/test_input/j_install_DE1.csv', 'tests/output_testfiles/translated_bde.csv')
# convert_test_file2('tests/test_input/j_install_DE1.csv', 'tests/output_testfiles/translated_bde1.csv', 'w')
# convert_test_file2('tests/test_input/test.csv', 'tests/output_testfiles/translated_bde2.csv', 'a')