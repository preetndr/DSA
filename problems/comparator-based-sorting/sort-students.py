import sys

data = iter(sys.stdin.read().split())
it = lambda: next(data)

n = int(it())

arr = [(it(), int(it())) for _ in range(n)]

arr.sort(key= lambda x: (-x[1], x[0]))

sys.stdout.write('\n'.join(' '.join(map(str, i)) for i in arr))


