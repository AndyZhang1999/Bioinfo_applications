"""
This is the test script for Assignment4
This script is called test_my_io.py
"""
import os
import pytest
from assignment4.my_io import get_fh


def test_existing_get_fh_4_reading():
    """Test for reading"""
    # Does it open a file for read
    # Open a file first
    _create_empty_test_file()
    test1 = get_fh(file='testfile5.txt', mode="r")

    # Verify the function
    assert hasattr(test1, "readline") is True, "Not able to open for reading"
    test1.close()
    os.remove('testfile5.txt')


def test_existing_get_fh_4_writing():
    """test for writing"""
    # Does it open a file to write
    # # Open a file first
    _create_empty_test_file()
    test = get_fh(file='testfile5.txt', mode="w")

    # Verify it
    assert hasattr(test, "write") is True, "Not able to open for writing"
    test.close()
    os.remove('testfile5.txt')


def test_get_fh_4_ioerror():
    """Test for IOerror"""
    with pytest.raises(IOError):
        # Try open a file not exist
        get_fh("nosuchfile.txt", "r")


def test_get_fh_4_valueerror():
    """Test for ValueError"""
    _create_empty_test_file()
    with pytest.raises(ValueError):
        get_fh("testfile5.txt", "skr")
    os.remove('testfile5.txt')


def _create_empty_test_file():
    open('testfile5.txt', "w").close()
