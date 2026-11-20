import sys

data = list(map(int, sys.stdin.read().split()))

n = data[0]
k = data[1]
arr = data[2:]

sum = 0
for i in range(k):
    sum += arr[i]

max_sum = sum

for i in range(k, n):
    sum += arr[i]
    sum -= arr[i - k]

    max_sum = sum if sum > max_sum else max_sum

sys.stdout.write(str(max_sum))
