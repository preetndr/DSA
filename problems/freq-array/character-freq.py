import sys

s = sys.stdin.readline().strip()
k = 26
a_ascii = ord('a')

freq_array = [0] * k

for i in s:
    freq_array[ord(i) - a_ascii] += 1
    
print('\n'.join((f"{chr(a_ascii + i)}:{freq_array[i]}") for i in range(k) if freq_array[i]))