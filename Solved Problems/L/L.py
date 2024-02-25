line = input().split()
N = int(line[0])
ans = int(line[1])
for i in range(1, N+1):
    line = input().split()
    if int(line[0]) <= ans <= int(line[1]):
        ans += 1
print(ans)