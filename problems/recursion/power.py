import sys

sys.setrecursionlimit(200000)


def solve(x, n):
    if n == 0:
        return 1

    ans = solve(x, n // 2) * solve(x, n // 2)

    if n % 2 == 0:
        return ans
    else:
        return x * ans


def main():
    x, n = list(map(int, sys.stdin.read().split()))
    sys.stdout.write(str(solve(x, n)))


if __name__ == "__main__":
    main()
