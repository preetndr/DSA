import sys

data = map(int, sys.stdin.read().split())

K = int(1e5 + 1)
n = next(data)

freq_arr = [0] * K

for i in data:
    freq_arr[i] += 1

result = ' '.join(str(i) for i in range(K) if freq_arr[i] > 1)

sys.stdout.write(result if result else '-1')
