"""
#  File: intersection.py
#  History: 2021/11/03 17:00 GMT
This is the solutions of the Assignment 4,, question 3.
IF you want to check the output of this program,
make sure run this program first (not the test script)
"""
import sys
import argparse
import os
from assignment4.my_io import get_fh


def get_list(fh_in):
    """
    fh_in : a file ready to be used in this function
    Takes : 1 arguments. The file from file handle
    @parameter: A file ready to be processed in this function
    @return: a list
    """
    # Generate a empty list first
    list0 = []
    # Add the first column into the list
    for line in fh_in:
        list0.append(line.split('\t')[0])

    # Remove the header line
    list0.remove(list0[0])

    return list0


def _remove_repeat_items(list3):
    """
    list3 : the list from last step
    Takes : 1 arguments. The list.
    @parameter: a list ready to be check
    @return: a list
    """
    # To take off the repeat element in the list
    uniq_list = list(set(list3))

    return uniq_list


def samenum(list1, list2):
    """
    list1,listt2 : two lists from last steps
    Takes : 2 arguments.2 lists
    second input file respectively
    @parameter: 2 lists. First one for input file 1,
    second for input file2
    @return: length of list1 and list two, the number of
    same element in two lists
    """
    # First clean up two lists
    list4 = _remove_repeat_items(list1)
    list5 = _remove_repeat_items(list2)

    # Get lenth
    len1 = len(list4)
    len2 = len(list5)

    # Get the number of same elements in two lists
    num = 0
    for item, _ in enumerate(list4):
        for index, _ in enumerate(list5):
            if list4[item] == list5[index]:
                num = num+1

    return len1, len2, num


def common(list6, list7):
    """
    list1,list2 : two lists from last steps
    Takes : 2 arguments.2 lists
    second input file respectively
    @parameter: 2 lists. First one for input file 1,
    second for input file2
    @return: new list of same genes in two lists
    """
    # Clean up two lists make sure no repeat genes
    list8 = _remove_repeat_items(list6)
    list9 = _remove_repeat_items(list7)

    # Append the same items into a new list
    new_list = []
    for element in list8:
        if element in list9:
            new_list.append(element)

    return new_list


def make_file1(new_list):
    """
    new_list : One list from last step
    Takes : 1 arguments. The new list only
    @parameter: 1 list.
    @return: an output file
    """
    # Set the path first
    save_path = './OUTPUT'
    finalfile = os.path.join(save_path, 'intersection_output.txt')
    # Since we want the result in order
    new_list.sort()

    # Make file
    fh_out = get_fh(finalfile, 'w')
    for i in new_list:
        fh_out.writelines(i)
        fh_out.writelines('\n')
    fh_out.close()


def get_cli_args():
    """
     Just get the command line options using argparse
    :return:Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Provide two gene\
     list (ignore header line), find intersection')

    parser.add_argument('-i1', '-infile1', dest='infile1',
                        type=str, help='Gene list 1 to open', required=True)
    parser.add_argument('-i2','-infile2',dest='infile2',
                        type=str, help='Gene list 2 to open', required=False)

    return parser.parse_args()


def main():
    """Business Logic"""
    args = get_cli_args()
    infile1 = args.infile1
    infile2 = args.infile2
    fh_in1 = get_fh(file=infile1, mode="r")
    fh_in2 = get_fh(file=infile2, mode="r")

    # Get two lists
    finallist_1 = get_list(fh_in1)
    finallist_2 = get_list(fh_in2)

    # Get the info we want to print
    len_1, len_2, num1 = samenum(finallist_1, finallist_2)
    list_new = common(finallist_1, finallist_2)
    make_file1(list_new)

    # Print the output
    print(f'\nNumber of unique gene names in ', args.infile1, f':', len_1, file=sys.stdout)
    print(f'Number of unique gene names in ', args.infile2, f':', len_2, file=sys.stdout)
    print(f'Number of common gene symbols found :', num1, file=sys.stdout)
    print(f'Output stored in OUTPUT/intersection_output.txt', file=sys.stdout)


if __name__ == '__main__':
    main()
