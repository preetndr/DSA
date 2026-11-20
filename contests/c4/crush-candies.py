import sys


# ===================== Implement this =====================
class CandyCollection:
    def __init__(self, maxOps: int):
        # TODO: sieve primes up to maxOps, init counts
        self.hash_map = {}
        self.count = 0
        pass

    def isPrime(self, j):
        n = self.hash_map.get(j, 0)
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def add(self, x: int) -> None:
        # TODO

        if self.isPrime(x):
            self.count -= 1
        self.hash_map[x] = self.hash_map.get(x, 0) + 1
        if self.isPrime(x):
            self.count += 1

    def remove(self, x: int) -> None:
        # TODO
        if self.hash_map.get(x, 0):
            if self.isPrime(x):
                self.count -= 1
            self.hash_map[x] -= 1
            if self.isPrime(x):
                self.count += 1
        else:
            self.hash_map.pop(x, None)

    def removeAll(self, x: int) -> None:
        if self.isPrime(x):
            self.count -= 1
        self.hash_map.pop(x, None)

    def countSpecial(self) -> int:
        # TODO
        return self.count


# ===================== I/O driver (do not modify) =====================
def main():
    data = sys.stdin.buffer.read().split()
    Q = int(data[0])
    pos = 1
    col = CandyCollection(Q)
    out = []
    for _ in range(Q):
        t = int(data[pos])
        pos += 1
        if t == 4:
            out.append(col.countSpecial())
        else:
            x = int(data[pos])
            pos += 1
            if t == 1:
                col.add(x)
            elif t == 2:
                col.remove(x)
            else:
                col.removeAll(x)
    print("\n".join(map(str, out)))


main()
