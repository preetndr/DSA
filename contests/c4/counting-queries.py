import sys


# ===================== Implement this =====================
class Solution:
    # queries[i] = (t, x)

    def countingQueries(
        self, a: list[int], queries: list[tuple[int, int]]
    ) -> list[int]:
        ans = []
        a.sort()

        for query in queries:
            first_occ = len(a)
            last_occ = -1
            q = query[0]
            x = query[1]

            if q == 1 or q == 2:
                l = 0
                r = len(a) - 1
                while l <= r:
                    mid = (r + l) // 2
                    if a[mid] >= x:
                        first_occ = mid
                        r = mid - 1
                    else:
                        l = mid + 1

            if q == 1 or q == 3:
                l = 0
                r = len(a) - 1
                while l <= r:
                    mid = (r + l) // 2
                    if a[mid] <= x:
                        last_occ = mid
                        l = mid + 1
                    else:
                        r = mid - 1

            if q == 1:
                ans.append(last_occ - first_occ + 1)
            elif q == 2:
                ans.append(first_occ)
            else:
                ans.append(len(a) - last_occ - 1)

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
    res = Solution().countingQueries(a, queries)
    print("\n".join(map(str, res)))


main()
