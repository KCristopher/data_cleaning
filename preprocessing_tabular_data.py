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
