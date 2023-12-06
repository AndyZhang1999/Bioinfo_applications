"""
This is the test script for the nucleotide_statistics_from_fasta.py
This program called test_nucleotide_statistics_from_fasta.py
"""
import pytest

from nucleotide_statistics_from_fasta import get_fh, get_header_and_sequence_lists, _check_size_of_lists,\
    _get_nt_occurance, _get_accession, print_sequence_stats


def test_print_sequence_stats():
    """Test if we have the correct file format and output"""
    # Just generate 2 lists
    list_headers = ['>101M:A:sequence']
    list_seqs = ['ACATGAATGNA']
    fh_out = 'testfile.txt'
    # Using the imported function
    print_sequence_stats(list_headers, list_seqs, fh_out)
    file = []

    # Put them to the file
    with open(fh_out, 'r') as out:
        for i in out:
            file.append(i)
    # Verify if the file is correct, output should like these 2 lines
    assert file[0] == "Number\tAccession\tA's\tG's\tC's\tT's\tN's\tLength\tGC%\t\n"
    assert file[1] == "1\t101M:A:sequence\t5\t2\t1\t2\t1\t11\t30.0%\t\n"


def test_get_fh_4_ioerror():
    """Test for IOerror"""
    with pytest.raises(IOError):
        get_fh("nosuchfile.txt", "r")


def test_get_fh_4_valueerror():
    """Test for ValueError"""
    with pytest.raises(ValueError):
        get_fh("influenza.fasta", "skr")


def test_get_header_and_sequence_lists():
    """Test if the header and sequence list is same"""
    list_header1, list_seq1 = get_header_and_sequence_lists('influenza.fasta')
    assert len(list_header1) == len(list_seq1)

    # Using the wrong file and try again
    list_header2, list_seq2 = get_header_and_sequence_lists('ss_designed2Fail.txt')
    assert len(list_header2) != len(list_seq2)


def test_get_nt_occurance():
    """Check if the get_nt_occurance function works"""
    list_seqs3 = ['A', 'C', 'A', 'T', 'G', 'A', 'A', 'T', 'G', 'N', 'A']
    # First check the number if it is correct
    assert _get_nt_occurance('A', list_seqs3) == 5
    assert _get_nt_occurance('T', list_seqs3) == 2
    assert _get_nt_occurance('G', list_seqs3) == 2
    assert _get_nt_occurance('N', list_seqs3) == 1
    assert _get_nt_occurance('C', list_seqs3) == 1

    # Then using some wrong character to double check
    with pytest.raises(SystemExit):
        _get_nt_occurance('K', list_seqs3)
    with pytest.raises(SystemExit):
        _get_nt_occurance('L', list_seqs3)
    with pytest.raises(SystemExit):
        _get_nt_occurance('E', list_seqs3)
    with pytest.raises(SystemExit):
        _get_nt_occurance('P', list_seqs3)
    with pytest.raises(SystemExit):
        _get_nt_occurance('AT', list_seqs3)


def test_get_accession():
    """Test if the get accession can work correctly"""
    header_string = '>EU521893 A/Arequipa/FLU3833/2006 2006// 4 (HA)'
    # See if we have desired output with self-made lists
    assert _get_accession(header_string) == '>EU521893'

    # One more try
    header_string2 = 'How about this one'
    assert _get_accession(header_string2) == 'How'


def test_check_size_of_lists():
    """Check if the check size function works"""
    list_headers4 = ['>101M:A:sequence', '>101M:A:secstr', '>102M:A:sequence']
    list_seqs4 = ['A', 'C', 'A', 'T', 'G', 'A', 'A', 'T', 'G', 'N', 'A']
    list_headers5 = ['>101M:A:sequence', '>101M:A:secstr']
    list_seqs5 = ['A', 'C']

    # The first one should not works second one should work
    assert not _check_size_of_lists(list_headers4, list_seqs4)
    assert _check_size_of_lists(list_headers5, list_seqs5)
