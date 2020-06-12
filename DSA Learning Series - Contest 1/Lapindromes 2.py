t = int(input())


for i in range(t):
    word = input()

    if len(word) % 2 == 0:
        firsthalf = word[0:len(word)//2]
        secondhalf = word[len(word)//2:]
    else:
        firsthalf = word[0:len(word) // 2]
        secondhalf = word[len(word) // 2 + 1:]
    letters1 = []
    letters2 = []

    for k in range(len(word)//2):
        letters1.append(firsthalf[k])
        letters2.append(secondhalf[k])

    letters1.sort()
    letters2.sort()
    if letters1 == letters2:
        print('YES')
    else:
        print('NO')