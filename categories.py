"""
#  File: categories.py
#  History: 2021/11/03 17:00 GMT
This is the solutions of the Assignment 4,, question 2.
IF you want to check the output of this program,
make sure run this program first (not the test script)
"""
import argparse
import os
from collections import defaultdict
from assignment4.my_io import get_fh
# pylint:disable=unused-variable
# I have to disable the 'unused-variable'
# in order to make sure the code can run or it will return
# 'ValueError: too many values to unpack'

def get_cli_args():
    """
     Just get the command line options using argparse
    :return:Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Combine on gene name'
                                                 ' and count the category occurrence')

    parser.add_argument('-i1', '--infile1', dest='infile1', type=str,
                        help='Path to the gene description file to open', required=True)
    parser.add_argument('-i2', '--infile2', dest='infile2', type=str,
                        help='Path to the gene category to open', required=True)

    return parser.parse_args()


def get_list_infile1(fh_in):
    """
    fh_in : a file ready to be used in this function
    Takes : 1 arguments. The file from file handle
    @parameter: A file ready to be processed in this function
    @return: a list
    """
    # Get an empty list first
    list1 = []
    for line in fh_in:
        (gene, des, cat) = line.split('\t')
        # Add item into the list after split the line
        list1.append(cat)

    return list1


def get_dict_infile1(list1):
    """
    list1 : a list ready to be used in this function
    Takes : 1 arguments. The list from last step
    @parameter: A list ready to be processed in this function
    @return: a dictionary
    """
    # Get a empty dictionary for later use
    dict1 = {}
    # Add the item in the list to the dictionary
    for i in list1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    return dict1


def process_dict_infile1(dict1):
    """
    dict1 : a dictionary of the chr21_genes.txt!
    Takes : 1 arguments. The dict from last step
    @parameter: A dict ready to be processed in this function
    @return: a dictionary ready for pairing the default dict later
    """
    # Get rid of the header line and newline
    del dict1['Category\n']
    del dict1['\n']

    # Then format the dict to make the key part
    # same as the dict of chr21_genes_categories.txt
    dict1['1.1'] = dict1.pop('1.1\n')
    dict1['5'] = dict1.pop('5\n')
    dict1['3.2'] = dict1.pop('3.2\n')
    dict1['2.2'] = dict1.pop('2.2\n')
    dict1['3.1'] = dict1.pop('3.1\n')
    dict1['4.2'] = dict1.pop('4.2\n')
    dict1['1.2'] = dict1.pop('1.2\n')
    dict1['4.1'] = dict1.pop('4.1\n')
    dict1['4.3'] = dict1.pop('4.3\n')
    dict1['2.1'] = dict1.pop('2.1\n')
    # Now we have a dict that can be used to make a default dict
    return dict1


def tackle_infile2_only(fh_in2):
    """
    fh_in2 : a file ready to be used in this function
    Takes : 1 arguments. The second input file from file handle
    @parameter: A file ready to be processed in this function
    @return: a dictionary
    """
    # Set an empty dict first
    dict2 = {}

    # Similaryly , get the dict of second input file
    for line in fh_in2:
        (cate, use) = line.split('\t')
        dict2[cate] = use

    return dict2


def get_dd(dict1, dict2):
    """
    dict1,dict2 : two dicts from last steps
    Takes : 2 arguments. 2 dicts of first and
    second input file respectively
    @parameter: 2 dicts. First one for input file 1,
    second for input file2
    @return: a default dictionary
    """
    # First generate the default dict
    default_dict = defaultdict(list)

    # Add stuff into the dd
    # Since we formatted the dict1 so we can just pair them easily here
    for element in (dict1, dict2):
        for key, value in element.items():
            default_dict[key].append(value)

    return default_dict


def make_file(default_dict):
    """
    dd : One default dict from last steps
    Takes : 1 arguments.
    @parameter: 1 dd.
    @return: a file
    """
    # We first set the path
    save_path = './OUTPUT'
    # Add the path
    finalfile1 = os.path.join(save_path, 'categories.txt')

    # Get a new list to write into the file
    list3 = ['Category', 'Occurrence', 'Description']
    file = get_fh(finalfile1, 'w')

    # Write stuff into the file
    # First write the header lines
    for index in list3:
        file.writelines('%s\t' % index)
    file.writelines('\n')

    # Then the context
    for key, val in default_dict.items():
        file.writelines(str(key))
        file.writelines('\t')
        file.writelines(str(val[0]))
        file.writelines('\t')
        file.writelines(str(val[1]))
    file.writelines('\n')
    file.close()


def main():
    """Business Logic"""
    args = get_cli_args()
    infile1 = args.infile1
    infile2 = args.infile2

    # Get two input file, Order matter!!
    fh_in1 = get_fh(file=infile1, mode="r")
    fh_in2 = get_fh(file=infile2, mode="r")

    # Process and format the first input file's dict
    list_1 = get_list_infile1(fh_in1)
    dict_1 = get_dict_infile1(list_1)
    new_dict1 = process_dict_infile1(dict_1)

    # Process the second input file
    dict_2 = tackle_infile2_only(fh_in2)

    # Make the dd
    new_dd = get_dd(new_dict1, dict_2)

    # Write file
    make_file(new_dd)


if __name__ == '__main__':
    main()
