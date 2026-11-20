import sys


# Implement only this function.
# Positions are numbered 1 to n: a[i - 1] is the element at position i.
# The element at position i (1 < i < n) is a critical point if it is greater
# than both of its neighbours or smaller than both of them.
# queries[k] = [L, R] asks how many critical points are at positions i with
# L < i < R. Return the answer for every query, in order.
def countCriticalPoints(a, queries):
    c_arr = [0] * n 
    result_arr = []
    
    for i in range(1, n - 1):
        left_element = a[i - 1]
        element = a[i]
        right_element = a[i + 1]
        if (element > left_element and element > right_element) or (element < left_element and element < right_element):
            c_arr[i] = 1
    
    for i in range(1, n):
        c_arr[i] += c_arr[i - 1]

    for q in queries:
        l, r = q[0] - 1, q[1] - 1
        if l == r:
            result_arr.append(0)
        else:
            result_arr.append(c_arr[r - 1] - c_arr[l])
    
    return result_arr


data = sys.stdin.buffer.read().split()
n, q = int(data[0]), int(data[1])
a = [int(x) for x in data[2:2 + n]]
pos = 2 + n
queries = [[int(data[pos + 2 * k]), int(data[pos + 2 * k + 1])] for k in range(q)]

print("\n".join(map(str, countCriticalPoints(a, queries))))