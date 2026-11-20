import sys

data = list(map(int, sys.stdin.read().split()))
n, m, k = data[0], data[1], data[2]
arr = data[3 : n + 3]
good_nums = set(data[n + 3 :])


def is_good(n):
    return True if n in good_nums else False


sum_ = sum(is_good(i) for i in arr[:k])
result = [sum_]

for i in range(k, n):
    sum_ -= is_good(arr[i - k])
    sum_ += is_good(arr[i])

    result.append(sum_)

sys.stdout.write(" ".join(map(str, result)))
