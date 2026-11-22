import sys


def solve():
    n = int(sys.stdin.readline().strip())

    left = 1
    right = n
    while left < right:
        mid = (left + right) // 2

        sys.stdout.write(f"? {left} {mid}\n")
        sys.stdout.flush()
        s = int(sys.stdin.readline().strip())

        if s:
            right = mid
        else:
            left = mid + 1

    sys.stdout.write(f"! {left}\n")
    sys.stdout.flush()


if __name__ == "__main__":
    solve()
