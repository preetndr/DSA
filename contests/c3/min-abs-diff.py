import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    arr, q, queries = sorted(data[1 : 1 + n]), data[1 + n], data[2 + n :]

    ans = []
    for i in range(q):
        x = queries[i]
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2

            if arr[mid] <= x:
                left = mid + 1
            else:
                right = mid - 1

        min_diff = float("inf")

        if left < n:
            min_diff = min(min_diff, abs(arr[left] - x))

        if left > 0:
            min_diff = min(min_diff, abs(arr[left - 1] - x))

        ans.append(str(min_diff))
    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    solve()
