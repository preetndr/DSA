import sys

data = list(map(int, sys.stdin.read().split()))

n, h_hours = data[0], data[1]

arr = data[2:]
k = None

left = 1
right = max(arr)

while left <= right:
    speed = (right + left) // 2

    total_hours = 0
    for pile in arr:
        total_hours += (pile + speed - 1) // speed

    if total_hours <= h_hours:
        k = speed
        right = speed - 1
    else:
        left = speed + 1

sys.stdout.write(str(k))
