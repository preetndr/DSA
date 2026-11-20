import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    next_Index = 1
    result = []

    for i in range(t):
        n, x = data[next_Index], data[next_Index + 1]

        arr = data[next_Index + 2 : next_Index + 2 + n]
        next_Index = next_Index + 2 + n

        left = 1
        right = max(arr) + x

        while left <= right:
            height = (left + right) // 2

            avail_water = x

            for coral in arr:
                avail_water -= height - coral if height > coral else 0

            if avail_water < 0:
                right = height - 1
            else:
                left = height + 1

        result.append(str(right))
    sys.stdout.write("\n".join(result))


if __name__ == "__main__":
    solve()
