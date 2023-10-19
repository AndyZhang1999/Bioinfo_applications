"""
This is the test script for the pdb_fasta_splitter.py
This program called test_pdb_fasta_splitter.py
"""
import pytest
from pdb_fasta_splitter import get_fh, get_header_and_sequence_lists, _check_size_of_lists, make_file


def test_get_fh_4_ioerror():
    """Test for IOerror"""
    with pytest.raises(IOError):
        get_fh("nosuchfile.txt", "r")


def test_get_fh_4_valueerror():
    """Test for ValueError"""
    with pytest.raises(ValueError):
        get_fh("ss.txt", "skr")


def test_get_header_and_sequence_lists():
    """Test if the header and sequence list is same"""
    list_header, list_seq = get_header_and_sequence_lists('ss.txt')
    assert len(list_header) == len(list_seq)

    # Using the wrong file and try again
    list_header2, list_seq2 = get_header_and_sequence_lists('ss_designed2Fail.txt')
    assert len(list_header2) != len(list_seq2)


def test_check_size_of_lists():
    """Check if the check size function works"""
    list_headers4 = ['>101M:A:sequence', '>101M:A:secstr', '>102M:A:sequence']
    list_seqs4 = ['A', 'C', 'A', 'T', 'G', 'A', 'A', 'T', 'G', 'N', 'A']
    list_headers5 = ['>101M:A:sequence', '>101M:A:secstr']
    list_seqs5 = ['A', 'C']

    # The first one should not works second one should work
    assert not _check_size_of_lists(list_headers4, list_seqs4)
    assert _check_size_of_lists(list_headers5, list_seqs5)


def test_make_file():
    """Test if we have the correct file format and output"""
    # First made 2 lists
    list_headers = ['>101M:A:sequence\n', '>101M:A:secstr\n']
    list_seq = ['MVLSEGYQG\n', 'HHHHHHHHHH GGGGGGT\n']
    elist = []
    elist2 = []

    # Use the function
    make_file(list_headers, list_seq)
    # Push all these lists into the new file
    with open('pdb_protein.fasta', 'r') as out:
        # Take out the stuff from the file into the elist to compare
        for i in out:
            elist.append(i)
    out.close()
    with open('pdb_ss.fasta', 'r') as out2:
        for i in out2:
            elist2.append(i)
    out2.close()

    # Verify the output
    assert elist[0] == '>101M:A:sequence\n'
    assert elist[1] == 'MVLSEGYQG\n'
    assert elist2[0] == '>101M:A:secstr\n'
    assert elist2[1] == 'HHHHHHHHHH GGGGGGT\n'



######
def test_mk_dict():
    # Get a file first
    _create_test_file1()
    # Use the fh
    file = get_fh('testfile1.txt','r')
    # Get the new dictionary here
    new_dc = mk_dict(file)

    assert new_dc == {'CYC1LP4': 'cytochrome c pseudogene'}
    file.close()
    os.remove('testfile1.txt')


def test_get_list_infile1():
    # Open the file
    _create_test_file1()

    # Get the file and open it to read
    infile2 = get_fh('testfile1.txt','r')
    list2 = get_list_infile1(infile2)

    assert list2[0] == '1.1\n'
    assert isinstance(list2, list) is True
    infile2.close()
    os.remove('testfile1.txt')

def test_get_dict_infile1():
    # check if the infile1 has the correct dict
    new_dict = get_dict_infile1(list0)

    assert new_dict == {'Category\n': 1, '\n': 1, '1.1': 1, '1.2': 2, '1.3': 1, '4.1': 2, '2.1': 1, '5': 1, '3.2': 1, '2.2': 1, '3.1': 1, '4.2': 1, '4.3': 1}
    assert isinstance(new_dict, dict) is True

def test_process_dict_infile1():
    # Similar to last one
    dict2 = process_dict_infile1(test_dict)
    assert dict2 == {'1.3\n': 12, '1.1': 1, '5': 12, '3.2': 1, '2.2': 1, '3.1': 10, '4.2': 71, '1.2': 2, '4.1': 31, '4.3': 1, '2.1': 12}
    assert isinstance(dict2, dict) is True

def test_tackle_infile2_only():
    # To see if the infile2 is correct
    _create_test_file2()
    # Open the file
    infile3 = get_fh("testfile4.txt","r")
    dict3 = tackle_infile2_only(infile3)

    assert dict3 == {'1.1': 'Genes with 100% identity over a complete cDNA with defined functional association (for example, transcription factor, kinase).\n', '1.2': 'Genes with 100% identity over a complete cDNA corresponding to a gene of unknown function (for example, some of the KIAA series of large cDNAs).\n'}
    assert isinstance(dict3, dict) is True
    infile3.close()
    os.remove('testfile4.txt')


def test_get_dd():
    # See if we have the correct dd
    dict4 = {'1.1': 1, '1.2': 1}
    dict5 = {'1.1': 'Genes with 100% identity over a complete cDNA with defined functional association (for example, transcription factor, kinase).', '1.2': 'Genes with 100% identity over a complete cDNA corresponding to a gene of unknown function (for example, some of the KIAA series of large cDNAs).'}
    new_dd = get_dd(dict4, dict5)

    assert new_dd == {'1.1': [1, 'Genes with 100% identity over a complete cDNA with defined functional association (for example, transcription factor, kinase).'], '1.2': [1, 'Genes with 100% identity over a complete cDNA corresponding to a gene of unknown function (for example, some of the KIAA series of large cDNAs).']}
    assert isinstance(new_dd, dict) is True

def test_make_file():
    # Check the output of the file
    list4 = []

    # Change the dir first
    os.chdir('../..')
    make_file(test_dd)
    out = get_fh('./OUTPUT/categories.txt', 'r')

    # Check the file
    for i in out:
        list4.append(i)

    assert os.path.isdir('./OUTPUT') is True
    assert os.path.exists('./OUTPUT/categories.txt') is True
    assert os.path.isfile('./OUTPUT/categories.txt') is True
    assert list4[0] == 'Category\tOccurrence\tDescription\t\n'


def test_get_list():
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
    # see if we have only the non-repeat element
    uniq_list = _remove_repeat_items(list9)

    assert uniq_list == [1, 2, 3]
    assert isinstance(uniq_list, list) is True


def test_samenum():
    # Ceck to see if the calculation is correct
    len1, len2, n = samenum(list0, list6)

    assert len1 == 13
    assert len2 == 8
    assert n == 8

def test_common():
    # Check if we have right output of common elmts in two lists
    list7 = common(list1, list9)

    assert list7 == [1, 2]
    assert isinstance(list7, list) is True

def test_make_file1():
    # Check the output file
    list8 = []
    # Change dir here
    make_file1(list6)
    out2 = get_fh('./OUTPUT/intersection_output.txt', 'r')
    # make file
    for item in out2:
        list8.append(item)

    assert os.path.isdir('./OUTPUT') is True
    assert os.path.exists('./OUTPUT/intersection_output.txt') is True
    assert os.path.isfile('./OUTPUT/intersection_output.txt') is True
    assert list8[0] == '1.1\n'
