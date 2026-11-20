import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))

    n, k = data[0], data[1]

    arr = data[2:]
    ret = None

    left = max(arr)
    right = sum(arr)

    if k > n:
        ret = -1
    else:
        while left <= right:
            pages = (left + right) // 2

            student = 1
            each_student_pages = 0
            doable = True

            for book in arr:
                if book <= pages - each_student_pages:
                    each_student_pages += book
                else:
                    student += 1
                    each_student_pages = book

                if student > k:
                    doable = False
                    break

            if doable:
                ret = pages
                right = pages - 1
            else:
                left = pages + 1

    sys.stdout.write(str(ret))


if __name__ == "__main__":
    solve()
