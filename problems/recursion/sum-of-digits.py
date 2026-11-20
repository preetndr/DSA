import sys

sys.setrecursionlimit(200000)


def solve(n):
    if n == 0:
        return 0

    return n % 10 + solve(n // 10)


def main():
    sys.stdout.write(str(solve(int(sys.stdin.read().strip()))))


if __name__ == "__main__":
    main()
