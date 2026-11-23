import sys

sys.setrecursionlimit(200000)


def solve(n):

    if not n:
        return 0

    return solve(n[:-1]) + (1 if n[-1] == "0" else 0)


def main():
    n = sys.stdin.read().strip()

    sys.stdout.write(str(solve(n)))


if __name__ == "__main__":
    main()
