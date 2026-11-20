import sys


def solve():
    data = list(sys.stdin.read().split())

    n = int(data[0])
    hash_map = {}
    result = []
    query_count = 0

    i = 0
    while query_count < n:
        i += 1
        query = data[i]

        if query == "active":
            result.append(str(len(hash_map)))
        else:
            i += 1
            movie = int(data[i])
            if query == "vote":
                hash_map[movie] = hash_map.get(movie, 0) + 1
            elif query == "withdraw" and movie in hash_map:
                hash_map[movie] -= 1
                if hash_map[movie] == 0:
                    del hash_map[movie]
            elif query == "check":
                result.append(str(hash_map.get(movie, 0)))

        query_count += 1
    if hash_map:
        result.append(
            "movie for tonight is "
            + (str(max(hash_map, key=lambda x: (hash_map[x], -x))))
        )
    if result:
        sys.stdout.write("\n".join(result))


if __name__ == "__main__":
    solve()
