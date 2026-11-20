import sys

data = list(map(int, sys.stdin.read().split()))
n, k, t, arr = data[0], data[1], data[2], data[3:]

good_count = 0
sum = 0
for i in range(k):
    sum += arr[i]

if sum / k >= t:
    good_count += 1

for i in range(k, n):
    sum += arr[i]
    sum -= arr[i - k]

    if sum / k >= t:
        good_count += 1

sys.stdout.write(str(good_count))
