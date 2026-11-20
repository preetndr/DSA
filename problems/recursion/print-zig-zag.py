import sys

sys.setrecursionlimit(100000)


def solve(n):
    if n == 0:
        return

    sys.stdout.write(str(n) + "\n")
    solve(n - 1)

    if n == 1:
        return
    sys.stdout.write(str(n) + "\n")


def main():
    solve(int(sys.stdin.read().strip()))


if __name__ == "__main__":
    main()
