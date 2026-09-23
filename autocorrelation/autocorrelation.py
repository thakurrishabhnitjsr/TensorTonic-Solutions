def autocorrelation(series: list, max_lag: int) -> list:
    import statistics as s
    x_var=0
    n=len(series)
    x_mean=s.mean(series)
    for i in series:
        x_var=x_var+((i-x_mean)**2)
    if x_var==0: return [1.0] + [0.0] * max_lag
    ans=[]
    for i in range(max_lag+1):
        xans=0
        for j in range(n-i):
            xans=xans+((series[j]-x_mean)*(series[j+i]-x_mean))
        ans.append(xans/x_var)
    return ans
    pass