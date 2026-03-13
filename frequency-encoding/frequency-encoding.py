from collections import defaultdict
def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    d = defaultdict(float)
    S = set(values)
    ans = [0]*len(values)
    for s in S:
        d[s] = values.count(s)/len(values)
    for i in range(len(values)):
        ans[i] = d[values[i]]
    return ans