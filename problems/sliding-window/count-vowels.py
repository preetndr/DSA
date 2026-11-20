import sys

data = sys.stdin.read().split()

n, k, s = int(data[0]), int(data[1]), data[2].lower()

vowels_set = {"a", "e", "i", "o", "u"}
count = 0

for i in range(k):
    if s[i] in vowels_set:
        count += 1

result = [count]

for i in range(k, n):
    if s[i] in vowels_set:
        count += 1
    if s[i - k] in vowels_set:
        count -= 1

    result.append(count)

sys.stdout.write(" ".join(map(str, result)))
