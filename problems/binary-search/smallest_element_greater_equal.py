import sys

data = list(map(int, sys.stdin.read().split()))
n, q = data[0], data[1]
arr = sorted(data[2 : n + 2])
queries = data[n + 2 :]


def search(ans):
    left = 0
    right = n - 1
    ret = -1

    while left <= right:
        mid = (right + left) // 2
        mid_element = arr[mid]

        if mid_element == ans:
            return mid_element
        elif mid_element < ans:
            left = mid + 1
        else:
            ret = mid_element
            right = mid - 1

    return ret


result = []

for i in queries:
    result.append(str(search(i)))

sys.stdout.write("\n".join(result))
