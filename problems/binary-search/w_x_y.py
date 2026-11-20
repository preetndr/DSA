import sys

data = list(map(int, sys.stdin.read().split()))
n, q = data[0], data[1]
arr = sorted(data[2 : n + 2])
queries = data[n + 2 :]


def search(ans, low):
    left = 0
    right = n - 1
    ret = n + 1 if low else -1

    while left <= right:
        mid = (right + left) // 2

        if low:
            if arr[mid] >= ans:
                ret = mid
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] <= ans:
                ret = mid
                left = mid + 1
            else:
                right = mid - 1

    return ret


result = []
for i in range(0, q * 2, 2):
    x = search(queries[i], low=True)
    y = search(queries[i + 1], low=False)
    result.append(str(0 if x > y else (y - x + 1)))

sys.stdout.write("\n".join(result))
