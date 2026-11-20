import sys

s = str(sys.stdin.readline().strip())

a_ascii = ord('a')
K = 26
freq_arr = [0] * K

for c in s:
    freq_arr[ord(c) - a_ascii] += 1
    
result = ''.join(chr(a_ascii + i) for i in range(K) if freq_arr[i] > 1)
    
    
sys.stdout.write(result if result else '-1')

