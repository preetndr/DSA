import sys

sys.setrecursionlimit(100000)


def solve(n):
    if n == 0:
        return

    solve(n - 1)
    sys.stdout.write(str(n) + "\n")


def main():
    solve(int(sys.stdin.read().strip()))


if __name__ == "__main__":
    main()
