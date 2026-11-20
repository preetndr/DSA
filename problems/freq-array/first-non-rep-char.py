import sys

s = str(sys.stdin.readline().strip())

a_ascii = ord('a')
K = 26
freq_arr = [0] * K
result = ''

for c in s:
    freq_arr[ord(c) - a_ascii] += 1

for c in s:
    if freq_arr[ord(c) - a_ascii] == 1:
        result = c
        break
    
sys.stdout.write(result if result else '-1')
    


