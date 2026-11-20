import sys

data = map(int, sys.stdin.read().split())

it = lambda: next(data)

n = it()

arr = [(it(), it(), it()) for _ in range(n)]

arr.sort(key= lambda x: (-x[2], x[1], x[0]))

sys.stdout.write('\n'.join(' '.join(map(str, x)) for x in arr))