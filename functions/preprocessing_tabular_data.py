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

def calc_leng_val_series(series) -> pd.Series :
    """
    Example
    -------
    print(calc_leng_val_series(pd.Series(['Alice', 'has', 'cat'])))

        0    5
        1    3
        2    3
        dtype: int64
        
    """
    return series.str.len()

def check_if_frames_are_equal(df_a, df_b) -> bool :
    """
    Checks if two dataframes are equal (have the same columns),
    regardless of the order of the columns.

    Parameters
    ----------
    df_a : pandas.DataFrame.
        First dataframe.
    df_b : pandas.DataFrame.
        Second dataframe.
    
    Returns
    -------
    bool.
        True if the dataframes are equal, False otherwise.
    
    Example
    -------
    df_a = pd.DataFrame({ 0: ['a', 'b', 'c'], 1: [9, 8, 7], 2: [True, True, False] })
    df_b = pd.DataFrame({ 0: [9, 8, 7], 1: [True, True, False], 2: ['a', 'b', 'c'] })
    df_c = pd.DataFrame({ 0: [9, 8, 7], 1: [True, True, False], 2: ['a', 'd', 'c'] })

    check_if_frames_are_equal(df_a, df_b)
        >>> True
    
    check_if_frames_are_equal(df_a, df_c)
        >>> False
    
    """
    
    return {tuple(df_a[c]) for c in df_a.columns} == {tuple(df_b[c]) for c in df_b.columns}

