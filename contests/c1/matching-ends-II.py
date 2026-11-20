import sys


# Implement only this function.
# Return the number of pairs (l, r) with 0 <= l <= r < n and
# colours[l] == colours[r]. A piece made of a single bead counts.
def countPrettyPieces(colours):
    freq = {}
    total = 0
    for i in colours:
        f = freq.get(i, 0) + 1
        freq[i] = f
        total += f
    return total
data = sys.stdin.buffer.read().split()
n = int(data[0])
colours = [int(x) for x in data[1:1 + n]]

print(countPrettyPieces(colours))