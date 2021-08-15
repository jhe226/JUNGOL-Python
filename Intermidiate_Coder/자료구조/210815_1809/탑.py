import sys

N = int(sys.stdin.readline())
towers = list(map(int, input().split()))
num = [0]*len(towers)
for i, tower in enumerate(towers):
    for j in range(i + 1, len(towers)):
        if towers[j]<tower:
            num[j] = i + 1
        else:
            break
print(*num)

