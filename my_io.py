"""This is the file handle """
import os
from assignment5.config import get_error_string_4_opening_file_OSError, \
    get_error_string_4_ValueError, get_error_string_4_TypeError


def get_fh(file=None, mode=None):
    """
      filehandle : get_fh(infile, "r")
      Takes : 2 arguments file name and mode i.e. what is needed to be done with
      this file. This function opens the file based on the mode passed in
      the argument and returns filehandle.
      @param file: The file to open for the mode
      @parm mode: They way to open the file, e.g. reading, writing, etc
      @return: filehandle
      """
    try:
        fobj = open(file, mode)
        return fobj
    except OSError:
        get_error_string_4_opening_file_OSError(file, mode)
        raise
    except ValueError:
        get_error_string_4_ValueError()
        raise
    except TypeError:
        get_error_string_4_TypeError()
        raise


def is_valid_gene_file_name(filename1_string):
    """
    filechecker : is_valid_gene_file_name(/path/to/the/file/name.unigene)
    Takes : 1 arguments file name with full path of
    this file. This function check the file to see if it is exist.
    @param filename path: The file path to open for the mode
    @return: T/F
    """
    if os.path.exists(filename1_string):
        return True
    return False
