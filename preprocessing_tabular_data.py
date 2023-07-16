import os
import re
import pandas as pd

def replace_trail_end_chara(series, chara = ' ') :

    """
    Parameters
    ----------
    series : pd.Series containing string values.

    Returns
    -------
    pd.Series.
    """

    return series.str.strip('{}'.format(chara))

def find_files_matching_pattern(levels_up, pattern, current_directory=None):
    """
    Returns a list of file paths matching a pattern recursively from
    a specified directory.

    Parameters
    ----------
    levels_up : int
        The number of levels to go up from the current directory.
    pattern : str
        The pattern to match file paths against.
    current_directory : str, optional
        The current directory path (default: None).

    Returns
    -------
    list
        A list of matched file paths.


    Example
    -------
    print(find_files_matching_pattern(1, r".+\.py$"))

        ['C:\\Users\\Predator\\Desktop\\data_cleaning\\data_cleaning\\
        preprocessing_tabular_data.py']
    
    """

    if current_directory is None:
        current_directory = os.getcwd()

    for _ in range(levels_up):
        current_directory = os.path.dirname(current_directory)

    matched_paths = []

    for root, dirs, files in os.walk(current_directory):
        for file in files:
            file_path = os.path.join(root, file)
            if re.match(pattern, file_path):
                matched_paths.append(file_path)

    return matched_paths
