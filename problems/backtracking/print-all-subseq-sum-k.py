import sys

sys.setrecursionlimit(100000)


def solve(n, sum, k, arr, ans, curr):
    if n == len(arr):
        if sum == k:
            ans.append(list(curr))
        return

    curr.append(str(arr[n]))
    solve(n + 1, sum + arr[n], k, arr, ans, curr)
    curr.pop()

    solve(n + 1, sum, k, arr, ans, curr)


def main():
    data = list(map(int, sys.stdin.read().split()))
    k, arr = data[1], data[2:]

    ans = []
    solve(0, 0, k, arr, ans, [])
    sys.stdout.write(str(len(ans)) + "\n")
    for a in ans:
        sys.stdout.write(" ".join(a) + "\n")


if __name__ == "__main__":
    main()
