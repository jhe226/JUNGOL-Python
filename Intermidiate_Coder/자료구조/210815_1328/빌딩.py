import sys

N = int(sys.stdin.readline())
H = []

for _ in range(N):
    H.append(int(sys.stdin.readline()))

stack = []
answer = []

for i in range(N-1, -1, -1):
    h = H[i]
    if stack:
        if stack[-1][0] > h:
            answer.append(stack[-1][1])
            stack.append((h, i+1))
        else:
            while stack and stack[-1][0] <= h:
                stack.pop()
            if stack:
                answer.append(stack[-1][1])
            else:
                answer.append(0)
            stack.append((h, i+1))

    else :
        answer.append(0)
        stack.append((h, i+1))

answer = list(reversed(answer))
for ans in answer:
    print(ans)