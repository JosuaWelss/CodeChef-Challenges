testcases = int(input())

for i in range(testcases):
    ladus = 0
    months = 0
    count, nation = map(str, input().split())
    for j in range(int(count)):
        valueList = input().split()
        if valueList[0] == 'CONTEST_WON':
            ladus = ladus + 300
            if int(valueList[1]) <= 20:
                ladus += 20-int(valueList[1])
        elif valueList[0] == 'TOP_CONTRIBUTOR':
            ladus = ladus + 300
        elif valueList[0] == 'BUG_FOUND':
            ladus = ladus + int(valueList[1])
        elif valueList[0] == 'CONTEST_HOSTED':
            ladus = ladus + 50
    if nation == 'INDIAN':
        months = ladus // 200
    else:
        months = ladus // 400
    print(months)
