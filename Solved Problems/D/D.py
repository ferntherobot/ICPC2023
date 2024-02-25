N = int(input())
ansFound = False
lst = [0] * N
for i in range(N):
    lst[i] = int(input())
for i in range(2, N+1):
    if N % i == 0:
        groupLen = N // i
        currentMax = max(lst[:groupLen])
        valid = True
        for j in range(groupLen, N, groupLen):
            if min(lst[j:j+groupLen]) > currentMax:
                currentMax = max(lst[j:j+groupLen])
            else:
                valid = False
                break
        if valid:
            print(i)
            ansFound = True
if not ansFound:
    print(-1)