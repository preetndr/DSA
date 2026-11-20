import sys

data = list(map(int, sys.stdin.read().split()))
n, k, arr = data[0], data[1], data[2:]

sum = 0
for i in range(k):
    sum += arr[i]

max_sum = sum + 1 if sum < k else sum

for i in range(k, n):
    if max_sum == k:
        break

    sum += arr[i]
    sum -= arr[i - k]

    flipped_sum = sum + 1 if sum < k else sum

    if flipped_sum > max_sum:
        max_sum = flipped_sum

sys.stdout.write(str(max_sum))
