import sys

data = map(int, sys.stdin.read().split())
it = lambda: next(data)

n = it()

arr = [(it(), it()) for i in range(n)]

arr.sort(key= lambda x: (x[0], x[1]))

sys.stdout.write('\n'.join(' '.join(map(str, i)) for i in arr))