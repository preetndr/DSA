import sys

data = iter(sys.stdin.read().split())

n = int(next(data))

sys.stdout.write('\n'.join(sorted(data, key= lambda x: (len(x), x))))