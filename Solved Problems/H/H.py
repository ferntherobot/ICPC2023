line = input()
valid = True
for _ in range(3):
    line = input()
    if not '7' in line:
        print(0)
        valid = False
        break
if valid:
    print(777)