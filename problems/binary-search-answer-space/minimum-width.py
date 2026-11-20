import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))

    n, m = data[0], data[1]
    arr = data[2:]

    left = max(arr)
    right = sum(arr) + len(arr) - 1
    ret = 0

    while left <= right:
        min_width = (left + right) // 2

        width_covered = arr[0]
        lines_covered = 1

        for word_width in arr[1:]:
            if 1 + word_width + width_covered <= min_width:
                width_covered += 1 + word_width
            else:
                lines_covered += 1
                width_covered = word_width

        if lines_covered > m:
            left = min_width + 1
        else:
            ret = min_width
            right = min_width - 1

    sys.stdout.write(str(ret))


if __name__ == "__main__":
    solve()
