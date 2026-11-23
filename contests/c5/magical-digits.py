import sys

sys.setrecursionlimit(200000)


def solve(digit):
    if len(digit) == 1:
        return digit

    return solve(str(sum(map(int, digit))))


def main():
    digit = sys.stdin.read().strip()

    sys.stdout.write(solve(digit))


if __name__ == "__main__":
    main()
