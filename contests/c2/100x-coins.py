import sys


def seq_cal(s):
    hash_map = {"lower": 0, "upper": 0, "amount": 0, "digit": 0}

    for c in s:
        if c >= "a" and c <= "z":
            hash_map["lower"] += 1
            hash_map["amount"] -= 2
        elif c >= "A" and c <= "Z":
            hash_map["upper"] += 1
            hash_map["amount"] += 3
        elif c >= "0" and c <= "9":
            hash_map["digit"] += 1
            hash_map["amount"] += int(c)

    return (
        -hash_map["amount"],
        -hash_map["digit"],
        hash_map["lower"],
        -hash_map["upper"],
        s,
    )


def solve():
    data = list(sys.stdin.read().split())

    sys.stdout.write(
        "\n".join(sorted(data[2:], key=lambda x: seq_cal(x))[: int(data[1])])
    )


if __name__ == "__main__":
    solve()
