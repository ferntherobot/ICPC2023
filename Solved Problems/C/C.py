line = input().split()
n = int(line[0])
d = int(line[1])
lst = [0] * n
for i in range(n):
    lst[i] = int(input())
lst.sort()
ans = 1
minVal = lst[0]
for i in lst:
    if (i - minVal) > d:
        minVal = i
        ans += 1
print(ans)