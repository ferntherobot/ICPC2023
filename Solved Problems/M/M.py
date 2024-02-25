val = input()
i = 0
j = 1
invalid = False
while i < len(val):
    #print(val[i:(i + len(str(i + 1)))])
    if int(val[i:(i + len(str(i + 1)))]) != j:
        invalid = True
        break

        
    i += len(str(i + 1))
    j += 1

if invalid:
    print(-1)

else:
    print(j - 1)