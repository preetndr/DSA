import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    arr, q, queries = data[1 : 1 + n], data[1 + n], data[2 + n :]

    ans = []
    for i in range(q):
        query = queries[i]
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2

            if arr[mid] <= query:
                right = mid - 1
            else:
                left = mid + 1

        ans.append(str(right + 1))

    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    solve()
