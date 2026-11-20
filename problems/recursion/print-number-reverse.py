import sys

sys.setrecursionlimit(100000)


def solve(n):
    if n == 0:
        return

    sys.stdout.write(str(n % 10))
    solve(n // 10)


def main():
    n = int(sys.stdin.read().strip())
    if n == 0:
        sys.stdout.write("0")
    else:
        solve(n)


if __name__ == "__main__":
    main()
