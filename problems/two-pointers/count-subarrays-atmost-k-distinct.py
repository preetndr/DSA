import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))
    n, k, arr = data[0], data[1], data[2:]

    sub_array_map = {}
    l = 0
    ans = 0

    for r in range(n):
        last_element = arr[r]
        sub_array_map[last_element] = sub_array_map.get(last_element, 0) + 1

        while len(sub_array_map) > k:
            initial_element = arr[l]
            sub_array_map[initial_element] -= 1

            if sub_array_map[initial_element] == 0:
                del sub_array_map[initial_element]

            l += 1

        ans += r - l + 1

    sys.stdout.write(str(ans))


if __name__ == "__main__":
    solve()
