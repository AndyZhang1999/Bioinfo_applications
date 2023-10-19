"""
This is the test script for Assignment4, Q1
This script is called test_chr21_gene_names.py
"""

import os
from chr21_gene_names import mk_dict
from assignment4.my_io import get_fh
STRING_1 = """TPTE\ttensin, putative protein-tyrosine phosphatas\
e, EC 3.1.3.48.\t1.1\nCYC1LP4\tcytochrome c pseudogene\t5\n"""


def test_mk_dict():
    """Test the first function here"""
    # Get a file first
    _create_test_file1()
    # Use the fh
    file = get_fh('testfile1.txt', 'r')
    # Get the new dictionary here
    new_dc = mk_dict(file)

    assert new_dc == {'CYC1LP4': 'cytochrome c pseudogene'}
    file.close()
    os.remove('testfile1.txt')


def _create_test_file1():
    file1 = open('testfile1.txt', "w")
    file1.write(STRING_1)
    file1.close()
