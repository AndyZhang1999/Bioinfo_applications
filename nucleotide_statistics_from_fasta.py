"""
This is the Assignment 3 question2
This programme is called nucleotide_statistics_from_fasta.py
"""
import sys
import argparse

# Set the global variable to use later
FLAG_2 = 1
FLAG_1 = 0

# pylint:disable=global-statement
# pylint:disable=line-too-long


def get_cli_driver():
    """
     Just get the command line options using argparse
    :return:Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Give the fasta sequence file name to get the nucleotide statistics')

    parser.add_argument('-i', '--infile', dest='infile', type=str, help='Path to the file to open', required=True)

    parser.add_argument('-o', '--outfile', dest='outfile', type=str, help='Path to the file to write', required=True)

    return parser.parse_args()


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


def _get_nt_occurance(str_dna, list_seqs4):
    """
    Input the dna string and the sequence list, out put T/F
    @param numbers: the dna string, sequence list
    @return: the occurance of the string in dna seq
    """
    if str_dna == 'A':
        return list_seqs4.count('A')
    if str_dna == 'G':
        return list_seqs4.count('G')
    if str_dna == 'C':
        return list_seqs4.count('C')
    if str_dna == 'T':
        return list_seqs4.count('T')
    if str_dna == 'N':
        return list_seqs4.count('N')
    if str_dna != ('A'or'G'or'C'or'T'or'N'):
        # If the str_dna is not one of above characters
        sys.exit(f"Did not code this condition")
    return None


def _get_accession(header_strings):
    """
    Input the header list, out put accession value
    @param numbers: the header list
    @return: accession value
    """
    global FLAG_2
    # Seperating the header list to make sure get the id number
    new_list = header_strings.split(' ')
    accession = new_list[0]
    # This will indicate the 'number', everytime use this function it will increase one
    FLAG_2 = FLAG_2 + 1
    return accession


def print_sequence_stats(list_headers5, list_seqs5, fh_out):
    """
    Input the header list and the sequence list,also the file to make the txt influenza file
    @param numbers: the header list, sequence list,file name
    @return: output a file
    """
    global FLAG_2
    with open(fh_out, "w") as outfile:
        for element in range(0, len(list_headers5)):
            # Using the function we defined before to get the values
            # accession = _get_accession(list_headers5[element])
            a_occur = _get_nt_occurance('A', list_seqs5[element])
            g_occur = _get_nt_occurance('G', list_seqs5[element])
            c_occur = _get_nt_occurance('C', list_seqs5[element])
            t_occur = _get_nt_occurance('T', list_seqs5[element])
            n_occur = _get_nt_occurance('N', list_seqs5[element])
            length = a_occur + g_occur + c_occur + t_occur + n_occur
            gc_percent = (g_occur + c_occur) / (a_occur + t_occur + g_occur + c_occur)

            # Generating 2 lists to create the file
            list1 = ["Number", "Accession", "A's", "G's", "C's", "T's", "N's", "Length", "GC%"]
            list2 = [FLAG_2, _get_accession(list_headers5[element])[1:], a_occur, g_occur,
                     c_occur, t_occur, n_occur, length, '{:.1%}'.format(gc_percent)]
            for i in list1:
                # Format the file
                outfile.writelines('%s\t' % (i))
            outfile.writelines('\n')
            for i in list2:
                outfile.writelines('%s\t' % (i))
            outfile.writelines('\n')
    outfile.close()


def main():
    """Business Logic"""
    # Using all the functions we defined before
    args = get_cli_driver()
    fh_in = args.infile
    fh_out = args.outfile
    list_headers, list_seqs = get_header_and_sequence_lists(fh_in)
    print_sequence_stats(list_headers, list_seqs, fh_out)


if __name__ == '__main__':
    main()
