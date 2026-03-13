def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    w = (max(values)-min(values))/num_bins
    ans = [0]*len(values)
    if w==0:
        return ans
        
    
    for i in range(len(values)):
        ans[i] = min(int((values[i]-min(values))/w), num_bins-1)
    return ans