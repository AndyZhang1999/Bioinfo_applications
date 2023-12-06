"""
This is the test script for Assignment4, Q1
This script is called test_chr21_gene_names.py
IF YOU RUN THIS SCRIPT THE FILE categories.txt in OUTPUT DIR
WILL BE THE TEST FILE FOR THIS SCRIPT, NOT THE OUTPUT OF THE categories.py!!
"""
import os
from categories import get_list_infile1, get_dict_infile1,\
    get_fh, process_dict_infile1, tackle_infile2_only, get_dd, make_file

# These are the materials we used for test
LIST_0 = ['Category\n', '\n', '1.1', '1.2', '1.3', '4.1', '2.1', '5',
          '3.2', '2.2', '3.1', '4.2', '4.1', '4.3', '1.2']
TEST_DICT = {'Category\n': 11, '\n': 10, '1.1\n': 1, '1.2\n': 2, '1.3\n': 12, '4.1\n': 31,
             '2.1\n': 12, '5\n': 12, '3.2\n': 1, '2.2\n': 1, '3.1\n': 10, '4.2\n': 71, '4.3\n': 1}
TEST_DD = {'1.1': [1, 'test line 1.'], '1.2': [1, 'test line 2).']}
STRING_1 = """TPTE\ttensin.\t1.1\nCYC1LP4\tcytochrome\t5\n"""
STRING_2 = """1.1\tGenes\n1.2\tDNAs\n"""

def test_get_list_infile1():
    """Check the list"""
    # Open the file
    _create_test_file1()

    # Get the file and open it to read
    infile2 = get_fh('testfile1.txt', 'r')
    list2 = get_list_infile1(infile2)

    assert list2[0] == '1.1\n'
    assert isinstance(list2, list) is True
    infile2.close()
    os.remove('testfile1.txt')


def test_get_dict_infile1():
    """check if the infile1 has the correct dict"""
    new_dict = get_dict_infile1(LIST_0)

    assert new_dict == {'Category\n': 1, '\n': 1, '1.1': 1, '1.2': 2, '1.3': 1, '4.1': 2, '2.1': 1, '5': 1, '3.2': 1,
                        '2.2': 1, '3.1': 1, '4.2': 1, '4.3': 1}
    assert isinstance(new_dict, dict) is True


def test_process_dict_infile1():
    """ Similar to last one"""
    dict2 = process_dict_infile1(TEST_DICT)
    assert dict2 == {'1.3\n': 12, '1.1': 1, '5': 12, '3.2': 1, '2.2': 1,
                     '3.1': 10, '4.2': 71, '1.2': 2, '4.1': 31, '4.3': 1, '2.1': 12}
    assert isinstance(dict2, dict) is True


def test_tackle_infile2_only():
    """ To see if the infile2 is correct"""
    _create_test_file2()
    # Open the file
    infile3 = get_fh("testfile4.txt", "r")
    dict3 = tackle_infile2_only(infile3)

    assert dict3 == {'1.1': 'Genes\n', '1.2': 'DNAs\n'}
    assert isinstance(dict3, dict) is True
    infile3.close()
    os.remove('testfile4.txt')


def test_get_dd():
    """ See if we have the correct dd """
    dict4 = {'1.1': 1, '1.2': 1}
    dict5 = {'1.1': 'Genes', '1.2': 'DNAs'}
    new_dd = get_dd(dict4, dict5)

    assert new_dd == ({'1.1': [1, 'Genes'], '1.2': [1, 'DNAs']})
    assert isinstance(new_dd, dict) is True


def test_make_file():
    """ Check the output of the file"""
    list4 = []

    # Change the dir first
    os.chdir('../..')
    make_file(TEST_DD)
    out = get_fh('./OUTPUT/categories.txt', 'r')

    # Check the file
    for i in out:
        list4.append(i)

    assert os.path.isdir('./OUTPUT') is True
    assert os.path.exists('./OUTPUT/categories.txt') is True
    assert os.path.isfile('./OUTPUT/categories.txt') is True
    assert list4[0] == 'Category\tOccurrence\tDescription\t\n'


def _create_test_file1():
    f_1 = open('testfile1.txt', "w")
    f_1.write(STRING_1)
    f_1.close()


def _create_test_file2():
    f_2 = open('testfile4.txt', "w")
    f_2.write(STRING_2)
    f_2.close()
