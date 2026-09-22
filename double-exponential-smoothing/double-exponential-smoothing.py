def double_exponential_smoothing(series: list, alpha: float, beta: float) -> list:
    """
    Returns the smoothed level at every time step.
    """
    level=series[0]
    trend=series[1]-series[0]
    levelx=[level]
    trendx=[trend]
    seriesx=[]
    for i in range(1,len(series)):
        level=alpha*series[i]+(1-alpha)*(levelx[i-1]+trendx[i-1])
        levelx.append(level)
        trend=beta*(levelx[i]-levelx[i-1])+(1-beta)*trendx[i-1]
        trendx.append(trend)
    return levelx
        
    pass