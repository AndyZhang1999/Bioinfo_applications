"""
#  File: chr21-gene_names.py
#  History: 2021/11/03 17:00 GMT
This is the solutions of the Assignment 4,, question 1.
"""
import sys
import argparse
from assignment4.my_io import get_fh

# I have to disable the 'unused-variable'
# in order to make sure the code can run or it will return
# 'ValueError: too many values to unpack, line 44'
# pylint:disable=unused-variable
# pylint:disable=global-statement
FLAG_1 = 1


def get_cli_args():
    """
     Just get the command line options using argparse
    :return:Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Open chr21_genes.txt, and'
                                                 ' ask user for a gene name')

    parser.add_argument('-i', '--infile', dest='infile', type=str,
                        help='Path to the file to open', required=True)

    return parser.parse_args()


def mk_dict(fh_in):
    """
dict0 : Get a dictionary from the input file
Takes : 1 arguments. The file from file handle
@parameter: A file ready to be processed in this function
@return: a dictionary
"""
    # First generate a empty dictionary and list for use
    dict0 = {}
    list1 = []

    # Read into the file from the file handle
    for line in fh_in:
        # Process the line , split them and give them value
        (gene, des, cat) = line.split('\t')
        # Connect the value from each lines and put them into dict0
        dict0[gene] = des
        # Add them to the list as well
        list1.append(gene)

    # Delete the first one, the header line
    del dict0[list1[0]]
    return dict0


def final_sys(new_dc):
    """
    print : the vary result according to the input name
    from use and the dict from last step
    Takes : 1 arguments. The dictionary from last step
    @parameter: A dictionary
    @return: Whether find the gene that user want or cease the program
    """
    # First claim this is a global value for use
    global FLAG_1

    # If satisfy the while condition:
    while FLAG_1 == 1:
        # Set a stopper to help print different string
        stopper = 0

        # Asking the user to input
        name = input(f'\nEnter gene name of interest. Type quit to exit: ')

        # Set the program terminate instruction
        if str(name).lower() == 'quit'.lower() or str(name).lower() == 'exit'.lower():
            print(f'Thanks for querying the data.', file=sys.stdout)
            # and we change the flag here to 0 to stop it
            FLAG_1 = 0
        else:
            for gene in new_dc:
                # When the input meet the name of gene in the dict we have
                if str(name) == gene:
                    # Change the stopper value to make diff with invalid input
                    stopper = 1
                    # Output strings
                    print(' ')
                    print(str(name), f'found! Here is the description:', file=sys.stdout)
                    print(new_dc[name], file=sys.stdout)

            # When the input can't match what we have in the dict
            if stopper == 0:
                print(f'Not a valid gene name.', file=sys.stdout)


def main():
    """Business Logic"""
    args = get_cli_args()
    infile = args.infile
    fh_in = get_fh(file=infile, mode="r")
    # Get the dictionary
    new_dict = mk_dict(fh_in)
    final_sys(new_dict)
    # Always close the file
    fh_in.close()


if __name__ == '__main__':
    main()
