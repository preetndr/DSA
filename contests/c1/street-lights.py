import sys


# Implement only this function.
# The street has n spots, numbered 0 to n - 1, where n is the length of
# power. If power[i] is 0 there is no lamp at spot i; otherwise the lamp
# lights every spot j with i - power[i] <= j`` <= i + power[i].
# Return the number of spots that no lamp lights.
def countDarkSpots(power):
    n = len(power)
    c_arr = [0] * n
    
    for i in range(n):
        if power[i] != 0:
            l = i - power[i]
            r = i + power[i]
            
            if l < 0:
                c_arr[0] += 1
            else:
                c_arr[l] += 1
            if r < n - 1:
                c_arr[r + 1] -= 1
            
            
    
    for i in range(1, n):
        c_arr[i] += c_arr[i - 1]
    
    dark_spots = 0
    for spot in range(n):
        if c_arr[spot] == 0:
            dark_spots += 1

    return dark_spots


data = sys.stdin.buffer.read().split()
n = int(data[0])
power = [int(x) for x in data[1:1 + n]]

print(countDarkSpots(power))