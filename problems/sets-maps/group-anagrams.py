import sys

data = iter(sys.stdin.read().split())

n = int(next(data))
di = {}

for s in data:
    di.setdefault(''.join(sorted(s)), []).append(s)
    
sorted_keys = sorted(di)

sys.stdout.write(str(len(di)) + '\n' + '\n'.join((str(len(di[key])) + ' ' + ' '.join(sorted(di[key]))) for key in sorted_keys))