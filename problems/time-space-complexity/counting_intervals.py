q = int(input().strip())
output = []

for _ in range(q):
    t, l, r = map(int, input().strip().split())
    
    if l > r:
        output.append(0)
    else:
        match t:
            case 1:
                if l == r:
                    output.append(0)
                else:
                    output.append(r - l - 1)
            case 2:
                output.append(r - l)
            case 3:
                output.append(r - l)
            case 4:
                output.append(r - l + 1)
            case _:
                output.append('Unknown')

print('\n'.join(map(str, output)))