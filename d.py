import pytest
import os
import sys
from chr21_gene_names import get_fh, mk_dict, final_sys
from categories import get_list_infile1, get_dict_infile1, get_fh, process_dict_infile1, tackle_infile2_only, get_dd, make_file
from intersection import get_list, samenum, common, make_file1, _remove_repeat_items
from assignment4.my_io import get_fh

#FILE_2_TEST = "test.txt"
list0 = ['Category\n', '\n', '1.1', '1.2', '1.3', '4.1', '2.1', '5', '3.2', '2.2', '3.1', '4.2', '4.1', '4.3', '1.2']#15
list6 = ['1.1', '1.2', '1.3', '4.1', '2.1', '5', '3.2', '2.2']
test_dict = {'Category\n': 11, '\n': 10, '1.1\n': 1, '1.2\n': 2, '1.3\n': 12, '4.1\n': 31, '2.1\n': 12, '5\n': 12, '3.2\n': 1, '2.2\n': 1, '3.1\n': 10, '4.2\n': 71, '4.3\n': 1}
test_dd = {'1.1': [1, 'test line 1.'], '1.2': [1, 'test line 2).']}
list9 = [1, 2, 3, 1, 2, 3]
list1 = [1, 2, 5, 6, 7]


def test_existing_get_fh_4_reading():
    #_create_test_file(FILE_2_TEST)
    test1 = get_fh(file='testfile3.txt', mode="r")
    assert hasattr(test1, "readline") is True, "Not able to open for reading"
    test1.close()


def test_existing_get_fh_4_writing():
    test = get_fh(file='testfile3.txt', mode="w")
    assert hasattr(test, "write") is True, "Not able to open for writing"
    test.close()


def test_get_fh_4_ioerror():
    """Test for IOerror"""
    with pytest.raises(IOError):
        get_fh("nosuchfile.txt", "r")


def test_get_fh_4_valueerror():
    """Test for ValueError"""
    with pytest.raises(ValueError):
        get_fh("testfile.txt", "skr")

def test_mk_dict():
    file = get_fh('testfile.txt','r')
    new_dc = mk_dict(file)
    assert new_dc == {'CYC1LP4': 'cytochrome c pseudogene'}

#def test_final_sys():

def test_get_list_infile1():
    infile2 = get_fh('testfile.txt','r')
    list2 = get_list_infile1(infile2)
    assert list2[0] == '1.1\n'
    assert isinstance(list2, list) is True

def test_get_dict_infile1():
    new_dict = get_dict_infile1(list0)
    assert new_dict == {'Category\n': 1, '\n': 1, '1.1': 1, '1.2': 2, '1.3': 1, '4.1': 2, '2.1': 1, '5': 1, '3.2': 1, '2.2': 1, '3.1': 1, '4.2': 1, '4.3': 1}
    assert isinstance(new_dict, dict) is True

def test_process_dict_infile1():
    dict2 = process_dict_infile1(test_dict)
    assert dict2 == {'1.3\n': 12, '1.1': 1, '5': 12, '3.2': 1, '2.2': 1, '3.1': 10, '4.2': 71, '1.2': 2, '4.1': 31, '4.3': 1, '2.1': 12}
    assert isinstance(dict2, dict) is True

def test_tackle_infile2_only():
    infile3 = get_fh("testfile2.txt","r")
    dict3 = tackle_infile2_only(infile3)
    assert dict3 == {'1.1': 'Genes with 100% identity over a complete cDNA with defined functional association (for example, transcription factor, kinase).\n', '1.2': 'Genes with 100% identity over a complete cDNA corresponding to a gene of unknown function (for example, some of the KIAA series of large cDNAs).\n'}
    assert isinstance(dict3, dict) is True


def test_get_dd():
    dict4 = {'1.1': 1, '1.2': 1}
    dict5 = {'1.1': 'Genes with 100% identity over a complete cDNA with defined functional association (for example, transcription factor, kinase).', '1.2': 'Genes with 100% identity over a complete cDNA corresponding to a gene of unknown function (for example, some of the KIAA series of large cDNAs).'}
    new_dd = get_dd(dict4, dict5)
    assert new_dd == {'1.1': [1, 'Genes with 100% identity over a complete cDNA with defined functional association (for example, transcription factor, kinase).'], '1.2': [1, 'Genes with 100% identity over a complete cDNA corresponding to a gene of unknown function (for example, some of the KIAA series of large cDNAs).']}
    assert isinstance(new_dd, dict) is True

def test_make_file():
    list4 = []
    os.chdir('../..')
    make_file(test_dd)
    #os.chdir('../..')
    out = get_fh('./OUTPUT/categories.txt', 'r')
    #with open('../../OUTPUT/categories.txt','r') as out:
    for i in out:
        list4.append(i)
    assert os.path.isdir('./OUTPUT') is True
    #assert os.path.isdir('./OUTPUT') is True
    assert os.path.exists('./OUTPUT/categories.txt') is True
    assert os.path.isfile('./OUTPUT/categories.txt') is True
    assert list4[0] == 'Category\tOccurrence\tDescription\t\n'


def test_get_list():
    infile4 = get_fh('testfile.txt', 'r')
    list5 = get_list(infile4)
    assert list5[0] == 'CYC1LP4'
    assert isinstance(list5, list) is True


def test_remove_repeat_items():
    uniq_list = _remove_repeat_items(list9)
    assert uniq_list == [1, 2, 3]
    assert isinstance(uniq_list, list) is True


def test_samenum():
    len1, len2, n = samenum(list0, list6)
    assert len1 == 13
    assert len2 == 8
    assert n == 8

def test_common():
    list7 = common(list1, list9)
    assert list7 == [1, 2]
    assert isinstance(list7, list) is True

def test_make_file1():
    list8 = []
    make_file1(list6)
    out2 = get_fh('./OUTPUT/intersection_output.txt', 'r')
    for item in out2:
        list8.append(item)
    assert os.path.isdir('./OUTPUT') is True
    # assert os.path.isdir('./OUTPUT') is True
    assert os.path.exists('./OUTPUT/intersection_output.txt') is True
    assert os.path.isfile('./OUTPUT/intersection_output.txt') is True
    assert list8[0] == '1.1\n'
