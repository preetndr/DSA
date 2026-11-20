import sys

n = int(sys.stdin.read().strip())

# if n == 0:
#     sys.stdout.write("0")
# else:
#     guess = int(n**0.5)

#     for i in range(guess + 1, guess - 2, -1):
#         if i <= n // i:
#             sys.stdout.write(str(i))
#             break

# Binary Search


def search(n):
    left = 1
    right = 10**9
    ret = 0

    if n == 0:
        return 0

    while left <= right:
        mid = (left + right) // 2

        if mid == n // mid:
            return mid

        elif mid < n // mid:
            ret = mid
            left = mid + 1

        else:
            right = mid - 1

    return ret


sys.stdout.write(str(search(n)))
