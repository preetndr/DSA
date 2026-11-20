import sys


# ===================== Implement this =====================
class Solution:
    # return an empty list if no zero-sum subarray exists
    def longestZeroSumSubarray(self, a: list[int]) -> list[int]:
        # TODO
        a = [0] + a
        sum = 0
        hash_map = {}
        ans = [0, 0]
        for r in range(len(a)):
            sum += a[r]
            if sum in hash_map:
                ans = max(ans, [hash_map[sum], r], key=lambda x: x[1] - x[0])
            hash_map.setdefault(sum, r)
        return a[ans[0] + 1 : ans[1] + 1]


# ===================== I/O driver (do not modify) =====================
def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = list(map(int, data[1 : 1 + n]))
    res = Solution().longestZeroSumSubarray(a)
    if not res:
        print(-1)
    else:
        print(" ".join(map(str, res)))


main()
