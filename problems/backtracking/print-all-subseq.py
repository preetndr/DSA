import sys

sys.setrecursionlimit(100000)


def solve(n, arr, curr=None):
    if curr is None:
        curr = []

    if n == len(arr):
        sys.stdout.write(" ".join(curr) + "\n")
        return

    curr.append(str(arr[n]))
    solve(n + 1, arr, curr)
    curr.pop()

    solve(n + 1, arr, curr)


def main():
    data = list(map(int, sys.stdin.read().split()))
    arr = data[1:]

    solve(0, arr)


if __name__ == "__main__":
    main()
