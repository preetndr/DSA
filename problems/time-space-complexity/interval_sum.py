q = int(input().strip())

for _ in range(q):
    l, r = map(int, input().strip().split())
    print(((r * (r + 1)) // 2) - ((l * (l - 1)) // 2))