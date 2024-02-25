count1 = 0
s = input()
while s:
    newS = ""
    charCount = {'A': 0, 'B': 0, 'C': 0}
    minCount = 0
    for c in s:
        if charCount[c] == minCount:
            charCount[c] += 1
            minCount = min(min(charCount['A'], charCount['B']), charCount['C'])
        else:
            newS += c
    s = newS
    count1+=1

print(count1)

