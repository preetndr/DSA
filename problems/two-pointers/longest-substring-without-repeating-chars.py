import sys


def solve():
    data = list(sys.stdin.read().split())

    n = int(data[0])
    arr = data[1]
    sub_string_map = {}
    l = r = 0
    ans = 0

    for c in arr:
        sub_string_map[c] = sub_string_map.get(c, 0) + 1

        while sub_string_map[c] > 1:
            initial_char = arr[l]
            sub_string_map[initial_char] -= 1

            if sub_string_map[initial_char] == 0:
                del sub_string_map[initial_char]

            l += 1

        ans = max(ans, r - l + 1)

        r += 1
    sys.stdout.write(str(ans))


if __name__ == "__main__":
    solve()
