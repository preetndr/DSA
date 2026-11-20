import sys

data = list(map(int, sys.stdin.read().split()))

n, x = data[0], data[1]
arr = sorted(data[2 : n + 2])
queries = data[n + 2 :]

result = []


def binary_search(ans):
    result = []

    for get_left in (True, False):
        l = 0  # noqa: E741
        r = n - 1
        res = None
        while l <= r:
            mid = (r + l) // 2

            curr_val = arr[mid]

            if get_left:
                if arr[mid] == ans:
                    res = mid + 1
                    r = mid - 1
                elif curr_val < ans:
                    l = mid + 1  # noqa: E741
                else:
                    r = mid - 1
            else:
                if arr[mid] == ans:
                    res = mid + 1
                    l = mid + 1
                elif curr_val <= ans:
                    l = mid + 1  # noqa: E741
                else:
                    r = mid - 1
        if res:
            result.append(res)
        else:
            return 0
    return result[1] - result[0] + 1


for i in queries:
    result.append(str(binary_search(i)))

sys.stdout.write("\n".join(result))
