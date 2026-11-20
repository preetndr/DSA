import sys

sys.setrecursionlimit(100000)


def solve(n, arr, ans, curr):
    if n == 0:
        ans.append(list(curr))
        return

    for num in range(n):
        curr.append(arr[num])
        solve(n - 1, arr[:num] + arr[num + 1 :], ans, curr)
        curr.pop()


def main():
    data = sys.stdin.read().split()
    n, arr = int(data[0]), data[1:]
    ans = []
    solve(n, arr, ans, [])
    sys.stdout.write(str(len(ans)) + "\n")

    for a in ans:
        sys.stdout.write(" ".join(a) + "\n")


if __name__ == "__main__":
    main()
