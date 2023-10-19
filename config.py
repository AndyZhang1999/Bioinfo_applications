""" This Module is used for configuration """

# Error" doesn't conform to snake_case naming style
# pylint: disable=invalid-name

_UNIGENE_DIR = "/data/PROGRAMMING/assignment5"
_UNIGENE_FILE_ENDING = "unigene"

def get_unigene_directory():
    """
        get the general path o the host dir
        @param : none
        @return: path to the database
    """
    return _UNIGENE_DIR


def get_unigene_extension():
    """
        get the file extension
        @param : None
        @return: ".unigene"
    """
    return _UNIGENE_FILE_ENDING


def get_host_keywords():
    """
        Get the dict for reference the avaliable search name for host
        @param : none
        @return: the host name that can be used refer to, and put them into the dictionary
    """
    bos_tarus = "Bos_taurus"
    Homo_sapiens = "Homo_sapiens"
    Equus_caballus = "Equus_caballus"
    Mus_musculus = "Mus_musculus"
    Ovis_aries = "Ovis_aries"
    Rattus_norvegicus = "Rattus_norvegicus"

    host_keywords = {
        "bos taurus": bos_tarus,
        "cow": bos_tarus,
        "cows": bos_tarus,
        "Homo sapiens": Homo_sapiens,
        "Human": Homo_sapiens,
        "Humans": Homo_sapiens,
        "Equus caballus": Equus_caballus,
        "Horse": Equus_caballus,
        "Horses": Equus_caballus,
        "Mus musculus": Mus_musculus,
        "Mouse": Mus_musculus,
        "mice": Mus_musculus,
        "Ovis aries": Ovis_aries,
        "Sheep": Ovis_aries,
        "Sheeps": Ovis_aries,
        "Rattus norvegicus": Rattus_norvegicus,
        "Rat": Rattus_norvegicus,
        "Rats": Rattus_norvegicus
    }
    # Get the dictionary
    return host_keywords


def get_error_string_4_ValueError():
    """
    Print the invalid argument message for ValueError
    """
    print("Invalid argument Value for opening a file for reading/writing")


def get_error_string_4_TypeError():
    """
    Print the invalid argument message for TypeError
    """
    print("Invalid argument Type passed in:")


def get_error_string_4_opening_file_OSError(file=None, mode=None):
    """
    Print the invalid argument message for OSError
    @param file1: The file name
    @param mode1: The mode to open the file
    """
    print(f"Could not open the file (os error): {file} with mode {mode}")
