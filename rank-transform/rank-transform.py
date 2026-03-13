from collections import defaultdict
def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    sorted_values = sorted(values)
    idx = [0]*len(values)
    left = 0
    d = defaultdict(float)
    while left<len(values):
        right = left
        while right<len(values) and sorted_values[right]==sorted_values[left]:
            right+=1
        index = (right+left-1)/2+1
        d[sorted_values[left]] = index
        left=right
    for i in range(len(idx)):
        idx[i] = d[values[i]]
    return idx
        
            


        
        

    