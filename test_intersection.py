"""
This is the test script for Assignment4, Q3
This script is called test_intersection.py
IF YOU RUN THIS SCRIPT THE FILE intersection_output.txt in OUTPUT DIR
WILL BE THE TEST FILE FOR THIS SCRIPT, NOT THE OUTPUT OF THE intersection.py!!
"""

import os
from intersection import get_list, samenum, common, make_file1, _remove_repeat_items
from assignment4.my_io import get_fh
# These are the materials we used for test
LIST0 = ['Category\n', '\n', '1.1', '1.2', '1.3', '4.1',
         '2.1', '5', '3.2', '2.2', '3.1', '4.2', '4.1', '4.3', '1.2']
LIST6 = ['1.1', '1.2', '1.3', '4.1', '2.1', '5', '3.2', '2.2']
TEST_DICT = {'Category\n': 11, '\n': 10, '1.1\n': 1, '1.2\n': 2, '1.3\n': 12, '4.1\n': 31, '2.1\n': 12,
             '5\n': 12, '3.2\n': 1, '2.2\n': 1, '3.1\n': 10, '4.2\n': 71, '4.3\n': 1}
TEST_DD = {'1.1': [1, 'test line 1.'], '1.2': [1, 'test line 2).']}
LIST9 = [1, 2, 3, 1, 2, 3]
LIST1 = [1, 2, 5, 6, 7]
STRING_1 = """TPTE\ttensin, putative protein-tyrosine phosphatas\
e, EC 3.1.3.48.\t1.1\nCYC1LP4\tcytochrome c pseudogene\t5\n"""


def test_get_list():
    """Test first function here"""
    # Get the list to see if it is correct
    _create_test_file1()
    # read the file
    infile4 = get_fh('testfile1.txt', 'r')
    list5 = get_list(infile4)

    assert list5[0] == 'CYC1LP4'
    assert isinstance(list5, list) is True
    infile4.close()
    os.remove('testfile1.txt')


def test_remove_repeat_items():
    """see if we have only the non-repeat element"""
    uniq_list = _remove_repeat_items(LIST9)

    assert uniq_list == [1, 2, 3]
    assert isinstance(uniq_list, list) is True


def test_samenum():
    """ Check to see if the calculation is correct"""
    len1, len2, num = samenum(LIST0, LIST6)

    assert len1 == 13
    assert len2 == 8
    assert num == 8


def test_common():
    """Check if we have right output of common elmts in two lists"""
    list7 = common(LIST1, LIST9)

    assert list7 == [1, 2]
    assert isinstance(list7, list) is True


def test_make_file1():
    """ Check the output file"""
    list8 = []
    # Change dir here
    make_file1(LIST6)
    out2 = get_fh('./OUTPUT/intersection_output.txt', 'r')
    # make file
    for item in out2:
        list8.append(item)

    assert os.path.isdir('./OUTPUT') is True
    assert os.path.exists('./OUTPUT/intersection_output.txt') is True
    assert os.path.isfile('./OUTPUT/intersection_output.txt') is True
    assert list8[0] == '1.1\n'


def _create_test_file1():
    file = open('testfile1.txt', "w")
    file.write(STRING_1)
    file.close()
