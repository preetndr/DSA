import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))

    n, k = data[0], data[1]

    arr = data[2:]
    ret = None

    left = max(arr)
    right = sum(arr)

    while left <= right:
        mid = (left + right) // 2

        painter = 1
        each_painter_time = 0
        doable = True

        for unit in arr:
            if unit <= mid - each_painter_time:
                each_painter_time += unit
            else:
                painter += 1
                each_painter_time = unit

            if painter > k:
                doable = False
                break

        if doable:
            ret = mid
            right = mid - 1
        else:
            left = mid + 1

    sys.stdout.write(str(ret))


if __name__ == "__main__":
    solve()
