import sys

data = iter(sys.stdin.read().split())
it = lambda: next(data)

a_ascii = ord('a')
K = 26
freq_arr = [0] * K

for c in it():
    freq_arr[ord(c) - a_ascii] += 1

for c in it():
    freq_arr[ord(c) - a_ascii] -= 1
    
if any(freq_arr):
    sys.stdout.write('NO')
else:
    sys.stdout.write('YES')
