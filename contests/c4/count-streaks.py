import sys


# ===================== Implement this =====================
class Solution:
    def countStreaks(self, a: list[int]) -> int:
        l = 0
        hash_map = {}
        ans = 0
        for r in range(len(a)):
            last_element = a[r]
            hash_map[last_element] = hash_map.get(last_element, 0) + 1

            while hash_map[last_element] > 1:
                initial_element = a[l]
                hash_map[initial_element] -= 1
                if hash_map[initial_element] == 0:
                    del hash_map[initial_element]

                l += 1

            ans += r - l + 1
        return ans


# ===================== I/O driver (do not modify) =====================
def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = list(map(int, data[1 : 1 + n]))
    print(Solution().countStreaks(a))


main()
