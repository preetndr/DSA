import sys

sys.setrecursionlimit(200000)


def solve(n, m, num, target):
    if target <= 1:
        return "0"

    if target == 2:
        return "1"

    if num == target:
        return str(m + n)

    return solve(m, n + m, num + 1, target)


def main():
    n = int(sys.stdin.read().strip())

    sys.stdout.write(solve(0, 1, 3, n))


if __name__ == "__main__":
    main()
