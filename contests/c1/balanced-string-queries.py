import sys


# Implement only this function.
# s contains only '0' and '1', and its characters are numbered 1 to n.
# queries[k] = [L, R] asks whether the substring from character L to
# character R contains as many zeros as ones.
# For every query, in order, return whether that substring is balanced.
def balancedQueries(s, queries):
    n = len(s)              # Bug 1: n was undefined
    q = len(queries) 
    p_sum = [0] * (n + 2)
    result = []
    
    for i in range(n):
        p_sum[i] += p_sum[i - 1] + int(s[i])
        
    for _ in range(q):
        l, r = queries[_]
        if (p_sum[r - 1] - p_sum[l - 2]) * 2 == (r - l + 1):
            result.append(True)
        else:
            result.append(False)
        
    return result


data = sys.stdin.buffer.read().split()
n, q = int(data[0]), int(data[1])
s = data[2].decode()
queries = [[int(data[3 + 2 * k]), int(data[4 + 2 * k])] for k in range(q)]

print("\n".join("YES" if ok else "NO" for ok in balancedQueries(s, queries)))