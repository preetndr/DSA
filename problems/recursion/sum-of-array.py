import sys

sys.setrecursionlimit(200000)


def solve(n, arr):
    if n == 0:
        return True
    if  
    ans = solve(n - 1, arr)
    return  <


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, arr = data[0], data[1:]

    sys.stdout.write(str(solve(n - 1, arr)))


if __name__ == "__main__":
    main()
