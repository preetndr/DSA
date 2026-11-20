import sys

data = map(int, sys.stdin.read().split())
it = lambda: next(data)

n = it()
hash_map = {it() for _ in range(n)}

m= it()
hash_map.update(it() for _ in range(m))

sys.stdout.write(str(len(hash_map)) + '\n' +' '.join(map(str, sorted(hash_map))))
