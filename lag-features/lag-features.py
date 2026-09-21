def lag_features(series: list, lags: list) -> list:
    """
    Returns the lag feature matrix.
    """
    xlist=[]
    for i in range(max(lags),len(series)):
        new_row=[]
        for j in lags:
            new_row.append(series[i-j])
        xlist.append(new_row)
    
    return xlist
    pass