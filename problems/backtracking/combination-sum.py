import sys

sys.setrecursionlimit(100000)


def solve(n, target, arr, ans, curr):
    if target == 0:
        ans.append(list(curr))
        return
    if target < 0 or n < 0:
        return

    curr.append(str(arr[n]))
    solve(n, target - arr[n], arr, ans, curr)
    curr.pop()

    solve(n - 1, target, arr, ans, curr)


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, target, arr = data[0], data[1], data[2:]
    ans = []
    solve(n - 1, target, arr, ans, [])
    sys.stdout.write(str(len(ans)) + "\n")

    for a in ans:
        sys.stdout.write(str(len(a)) + " " + " ".join(a) + "\n")


if __name__ == "__main__":
    main()
