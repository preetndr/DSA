import sys

data = map(int, sys.stdin.buffer.read().split())
it = lambda: next(data)

n = it()

ref_x, ref_y = it(), it()


arr = [(it(),it()) for _ in range(n)]

arr.sort(key= lambda i: (((i[0] - ref_x) ** 2 + (i[1] - ref_y) ** 2), i[0], i[1]))

sys.stdout.write('\n'.join(' '.join(map(str, x)) for x in arr))