import sys

data = sys.stdin.read().strip()

o_count = 0
result = 0

for ch in data:
    if ch == 'G':
        result += o_count
    elif ch == 'O':
        o_count += 1

sys.stdout.write(str(result))