import sys

sys.setrecursionlimit(200000)


def solve(n, a, b, c, moves):

    if n == 0:
        return

    solve(n - 1, a, c, b, moves)

    moves.append(f"Move {a} to {c}")

    solve(n - 1, b, a, c, moves)


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    moves = []
    arr, x = data[1:-1], data[-1]
    solve(n, "A", "B", "C", moves)
    sys.stdout.write("\n".join(moves))


if __name__ == "__main__":
    main()
