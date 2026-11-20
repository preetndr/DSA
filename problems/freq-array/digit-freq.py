import sys

k = 10
ascii_0 = ord('0')
num = sys.stdin.readline().strip()

freq_arr = [0] * k

for n in num:
    freq_arr[ord(n) - ascii_0] += 1
    
sys.stdout.write(' '.join(map(str, freq_arr)))