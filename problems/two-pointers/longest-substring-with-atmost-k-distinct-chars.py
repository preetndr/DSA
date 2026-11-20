import sys


def solve():
    data = list(sys.stdin.read().split())

    [n, k], st = map(int, data[:2]), data[2]
    sub_string_map = {}
    l = r = 0
    ans = 0

    for c in st:
        sub_string_map[c] = sub_string_map.get(c, 0) + 1

        while len(sub_string_map) > k:
            initial_char = st[l]
            sub_string_map[initial_char] -= 1

            if sub_string_map[initial_char] == 0:
                del sub_string_map[initial_char]

            l += 1

        ans = max(ans, r - l + 1)

        r += 1

    sys.stdout.write(str(ans))


if __name__ == "__main__":
    solve()
