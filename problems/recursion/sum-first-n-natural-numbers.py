import sys

sys.setrecursionlimit(200000)


def solve(n):
    if n == 0:
        return 0

    return n + solve(n - 1)


def main():
    n = int(sys.stdin.read().strip())
    sys.stdout.write(str(solve(n)))


if __name__ == "__main__":
    main()
