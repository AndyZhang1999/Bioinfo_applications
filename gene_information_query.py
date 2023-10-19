"""
This is the solution of assignment 5
the name of this program is gene_information_query.py
by YICHENG ZHANG
2021/11/25
"""
import sys
import re
import argparse
from assignment5.my_io import get_fh, is_valid_gene_file_name
from assignment5.config import get_unigene_directory, get_unigene_extension, get_host_keywords

# Have to disable this for line 107 or the function will return "TypeError: object of type 'NoneType' has no len()"
# pylint: disable=inconsistent-return-statements


def modify_host_name(host_name):
    """
        Modify the host name user entered
        @param : The host name
        @return: the modified host name refer to the dicionary
    """
    # First get the dict we need for reference
    name_dir = get_host_keywords()

    # Change all the dict keys to the lower case
    new_name_dir = {k.lower(): v for k, v in name_dir.items()}

    # make the entered hostname string
    new_name = str(host_name)

    # Assume we may have _ in the host name
    if "_" in new_name:

        # change all the _ to space as default
        parsed_newname = new_name.replace("_", " ")
        # Since this is case insensitive
        if parsed_newname.lower() in new_name_dir:

            # return a dir name that existed match with the entered host name
            return new_name_dir[parsed_newname.lower()]

        # get the helper function if no match
        _print_host_directories()
        sys.exit(1)

    # If no _ in the entered host name
    elif new_name.lower() in new_name_dir:
        return new_name_dir[new_name.lower()]
    # when no match
    else:
        _print_host_directories()
        sys.exit(1)


def _print_host_directories():
    """
        helper function when no match dir name with entered host name
        @param : none
        @return: the exisiting hostname option
    """
    # Get the host name keywords dict first
    dict1 = get_host_keywords()

    # Get empty dict&list
    dict2 = {}
    value_list = []
    key_list = []

    # To take out the value in the dict, and put them to a list
    for key, value in dict1.items():
        # Since we don't need repeat values
        if value not in dict2.values():
            dict2[key] = value
    for val in dict2.values():
        value_list.append(val)

    # Take out all the keys then
    for keys in dict1:
        key_list.append(keys)
    key_list2 = [all_keys.capitalize() for all_keys in key_list]
    key_list2.sort()

    # Print all the instruction and existing host name options
    print(" ", file=sys.stderr)
    print(f'\nEither the Host Name you are searching for is not in the database', file=sys.stderr)
    print(f"\nor If you are trying to use the scientific name please put the name in double quotes:", file=sys.stderr)
    print(f'\n"Scientific name"', file=sys.stderr)
    print(f'\nHere is a (non-case sensitive) list of available Hosts by scientific name\n', file=sys.stderr)
    for value_index, value_value in enumerate(value_list, start=1):
        print(f'{format(value_index):>3}. {value_value}', file=sys.stderr)
    print(" ", file=sys.stderr)
    print(f'\nHere is a (non-case sensitive) list of available Hosts by common name\n', file=sys.stderr)
    for key_index, key_value in enumerate(key_list2, start=1):
        print(f'{format(key_index):>3}. {key_value}', file=sys.stderr)


def get_gene_data(gene_filename):
    """
        open the gene file witht the path and take the tissue list out
        @param : The file path
        @return: the express tissue list in the gene file
    """
    # OPen the file first
    file = get_fh(file=gene_filename, mode="r")

    # Find out the EXPRESS line and take out the tissues
    for line in file:
        line = line.rstrip()
        match = re.search(r"EXPRESS\s+(.*)", line)

        # When find it:
        if match:
            tissue_string = match.group(1)
            # Since some tissues are splited by "| " but some are only"|"
            # We need to change both of these into "\t" in order to split them correctly
            parsed_string = tissue_string.replace("| ", "\t")
            parsed_string_again = parsed_string.replace("|", "\t")
            # Get the tissue list with the parsed tissue string now
            tissue_list2 = parsed_string_again.split("\t")
            # Sort it
            tissue_list2.sort()
            # Make all the first letter upper case
            tissue_list3 = [words.capitalize() for words in tissue_list2]
            return tissue_list3


def print_output(host, gene, sorted_list_tissue):
    """
        print the result
        @param : The host name, the gene name , the list of tissues
        @print: the result in with order number and lining up by the '.'
    """
    print(f'In {host}, There are {len(sorted_list_tissue)} tissues that {gene} is expressed in:\n')

    # To print out with order number and lining up by the .
    for index, value in enumerate(sorted_list_tissue, start=1):
        print(f'{format(index):>3}. {value}', file=sys.stderr)


def get_cli_args():
    """
     Just get the command line options using argparse
    :return:Instance of argparse arguments
    """
    parser = argparse.ArgumentParser(description='Give the Host and Gene name')

    parser.add_argument('-host', dest='HOST',
                        type=str, help='Name of Host', required=False, default="Homo sapiens")
    parser.add_argument('-gene', dest='GENE',
                        type=str, help='Name of Gene', required=False, default="TGM1")

    return parser.parse_args()


def main():
    """Business logic"""
    args = get_cli_args()
    raw_host = args.HOST
    gene = args.GENE
    # first parse the entered host name
    hosted = modify_host_name(raw_host)

    # Since there must be _ in the new host name after parse through the dict in config.py
    if "_" in str(hosted):
        # change the _ to " " for later use
        host = hosted.replace("_", " ")
        # Get the file path
        file = "/".join((get_unigene_directory(), hosted, gene + "." + get_unigene_extension()))

        # Check for the validation of the file path
        if is_valid_gene_file_name(file):
            print(f"\nFound Gene {gene} for {host}", file=sys.stderr)
            # get the tissue list now
            list_of_tissue = get_gene_data(file)
            # print output
            print_output(host, gene, list_of_tissue)

        # If not valid gene name
        else:
            print(f"Not found", file=sys.stderr)
            print(f"Gene {gene} does not exist for {host}. exiting now...", file=sys.stderr)
            sys.exit(1)


if __name__ == '__main__':
    main()
