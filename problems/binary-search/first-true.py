import sys


def interact(i):
    sys.stdout.write("? " + str(i) + "\n")
    sys.stdout.flush()
    return sys.stdin.readline().strip()


n = int(sys.stdin.readline().strip())

left = 1
right = n
ans = str(n + 1)

while left <= right:
    mid = (right + left) // 2

    if interact(mid) == "T":
        ans = str(mid)
        right = mid - 1
    else:
        left = mid + 1

sys.stdout.write("! " + ans)
