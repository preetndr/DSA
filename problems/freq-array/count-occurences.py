import sys

data = map(int, sys.stdin.read().split())

K = 1000 + 1
n = int(next(data))

freq_arr = [0] * K

for n in data:
    freq_arr[n] += 1
    
sys.stdout.write('\n'.join(f"{i} {freq_arr[i]}" for i in range(K) if freq_arr[i]))

