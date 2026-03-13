import statistics

def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    
    Args:
        values: List of numerical values
        
    Returns:
        Scaled values using (x - median) / IQR
    """
    if not values:
        return []
    
    
    median_val = statistics.median(values)
    

    sorted_vals = sorted(values)
    n = len(sorted_vals)
    if n==1:
        return [0]
    
    

    if n % 2 == 0:
        q1 = statistics.median(sorted_vals[:n//2])
        q3 = statistics.median(sorted_vals[n//2:])
    else:
        q1 = statistics.median(sorted_vals[:n//2])
        q3 = statistics.median(sorted_vals[n//2 + 1:])
    

    iqr = q3 - q1
    
 
    if iqr != 0:
        return [(x - median_val) / iqr for x in values]
    else:
        return [(x - median_val) for x in values]