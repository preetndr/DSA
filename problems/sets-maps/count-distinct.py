import sys

data = map(int, sys.stdin.read().split())

n = next(data)

hash_map = set()

for _ in range(n):
    hash_map.add(next(data))
    
sys.stdout.write(str(len(hash_map)))


