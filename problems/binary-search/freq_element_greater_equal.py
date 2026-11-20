import sys

data = list(map(int, sys.stdin.read().split()))
n, q = data[0], data[1]
arr = sorted(data[2 : n + 2])
queries = data[n + 2 :]


def search(ans):
    left = 0
    right = n - 1
    ret = None

    while left <= right:
        mid = (right + left) // 2

        if arr[mid] >= ans:
            ret = mid
            right = mid - 1
        else:
            left = mid + 1

    return ret


result = []
for i in queries:
    val = search(i)
    result.append(str(0 if val is None else n - val))

sys.stdout.write("\n".join(result))
