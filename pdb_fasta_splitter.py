"""
This is the Assignment 3 question1
This programme is called pdb_fasta_splitter.py
If you want to check the output of this file,
make sure you run THIS program before run the test program
of this file. Or the output file will be the file of test program!!!
"""
import sys
import re
import argparse

# Set the global variable to use later
FLAG_1 = 0

# pylint:disable=global-statement
# pylint:disable=line-too-long

def get_fh(file, mode):
    """
    Check if the file is avaliable and if the mode is correct
    @param numbers: the input file and the mode of it.
    @return: a file ready for processing
    """
    try:
        # Check If the mode of the file is correct
        if mode not in ('r', 'w'):
            raise ValueError
        # Starting reading file
        open(file, "r")

    except IOError:
        # This is because we can't find the input file
        raise IOError

    except ValueError:
        # When the mode of file is not 'w' or 'r'
        raise ValueError
    return file


def get_header_and_sequence_lists(infile):
    """Input a file and get 2 lists. One for seuqneces, one for the header
    @param numbers: the input file
    @return: 2 lists
    """
    # First initial 2 lists ready for using
    list_seq = []
    list_header = []
    # Set the empty str for list append
    empty_str = ''

    # Open the file
    with open(infile, 'r') as file:
        for line in file:
            if line.startswith('>'):
                # Find all the headers
                list_header.append(line)
                if empty_str != '':
                    list_seq.append(empty_str)
                    empty_str = ''
            else:
                empty_str = empty_str + line

        # Similarly with the last step
        if empty_str != '':
            list_seq.append(empty_str)
            empty_str = ''

        # this is for get rid of the newline character
        list_seqs = []
        for element in list_seq:
            list_seqs.append(element.strip())

    # Use the _check_size_of_lists function to verify if the file in right form
    if not _check_size_of_lists(list_header, list_seq):
        print(f'The size of the sequences and the header lists is different')
        print(f'Are you sure the FASTA is in correct format')
        global FLAG_1
        FLAG_1 = 1
        # Since the form is not right, change flag to 1 and stop the program
    return (list_header, list_seq)


def get_num(list_header1):
    """
    Input the header list we get from previous step
    @param numbers: the header list
    @return: print out how many SS and protein sequence found in the file
    """
    num_seq1 = 0
    num_secstr1 = 0
    for elements in list_header1:
        # Find all the headers end with the 'sequence'
        if re.match(".*sequence", elements):
            num_seq1 = num_seq1 + 1
    # All the rest should be ss sequence then
    num_secstr1 = len(list_header1) - num_seq1

    # Print out the result
    print(f'Found ', num_seq1, f' protein sequences', file=sys.stderr)
    print(f'Found', num_secstr1, f' ss sequences', file=sys.stderr)


def make_file(list_header2, list_seq2):
    """
    Input the header list and the sequence list, out put 2 files
    @param numbers: the header list, sequence list
    @return: The pdb_protein.fasta and pdb_ss.fasta
    """
    # Initializing 2 lists as usual
    file_seq = []
    file_secstr = []

    for index in range(0, len(list_header2)):
        if re.match('.*sequence', list_header2[index]):
            # Since the 2 lists should match with each other
            file_seq.append(list_header2[index])
            file_seq.append(list_seq2[index])
        else:
            # For ss sequence file
            file_secstr.append(list_header2[index])
            file_secstr.append(list_seq2[index])

    # Loading all the lists from above to the files
    with open("pdb_protein.fasta", "w") as outfile1:
        for index in file_seq:
            outfile1.writelines(index)
    outfile1.close()
    with open("pdb_ss.fasta", "w") as outfile2:
        for index in file_secstr:
            outfile2.writelines(index)
    outfile2.close()


def _check_size_of_lists(list_headers3, list_seqs3):
    """
    Input the header list and the sequence list, out put T/F
    @param numbers: the header list, sequence list
    @return: T/F
    """
    # Just check the length of them to make sure they canmatch each other
    if len(list_seqs3) == len(list_headers3):
        return True
    return False


def get_cli_driver():
    """
     Just get the command line options using argparse
    :return:Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Give the fasta sequence file name to do the splitting')
    parser.add_argument('-i', '--infile', dest='infile', type=str, help='Path to the file to open', required=True)
    return parser.parse_args()


def main():
    """Business Logic"""
    # Assembly all the functions
    args_1 = get_cli_driver()
    fh_in1 = get_fh(args_1.infile, "r")
    list_header, list_seq = get_header_and_sequence_lists(fh_in1)
    if FLAG_1 == 0:
        # If flag = 1 means the file is not in the right form
        make_file(list_header, list_seq)
        get_num(list_header)


if __name__ == '__main__':
    main()
