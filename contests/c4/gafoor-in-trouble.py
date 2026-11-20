import sys


# ===================== Implement this =====================
class Solution:
    # queries[i] = (L, R), 1-indexed inclusive
    def gafoorQueries(self, a: list[int], queries: list[tuple[int, int]]) -> list[int]:
        ans = []
        # TODO
        n = len(a)
        con_arr = [0] * (n + 1)
        sum_arr = [0] * (n + 1)

        for i in range(1, n + 1):
            if a[i - 1] % 10 in (1, 7):
                con_arr[i] = 1

        for i in range(1, n + 1):
            sum_arr[i] = sum_arr[i - 1] + con_arr[i]

        for l, r in queries:
            ans.append(sum_arr[r] - sum_arr[l - 1])

        return ans


# ===================== I/O driver (do not modify) =====================
def main():
    data = sys.stdin.buffer.read().split()
    n, q = int(data[0]), int(data[1])
    a = list(map(int, data[2 : 2 + n]))
    pos = 2 + n
    queries = []
    for _ in range(q):
        queries.append((int(data[pos]), int(data[pos + 1])))
        pos += 2
    res = Solution().gafoorQueries(a, queries)
    print("\n".join(map(str, res)))


main()
