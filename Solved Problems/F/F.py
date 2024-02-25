rolledDice = int(input())
diceLeft = 4 - rolledDice
possDiceLeft = 6 ** diceLeft
if len(set(input().split())) < rolledDice:
    print("0 " + str(possDiceLeft))
else:
    ashley = possDiceLeft
    for i in range(diceLeft):
        ashley = ashley * (6 - rolledDice - i) // 6
    print(str(ashley) + " " + str(possDiceLeft - ashley))