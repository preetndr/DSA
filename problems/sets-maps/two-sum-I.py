import sys

data = map(int, sys.stdin.read().split())

n, x = next(data), next(data)

seen_in_map = set()
    
result = False

for num in data:
    
    if (x - num) in seen_in_map:
        result = True
        break
    
    seen_in_map.add(num)

sys.stdout.write(str(result).upper())