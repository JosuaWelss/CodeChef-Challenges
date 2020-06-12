t = int(input())

for i in range(t):
    teamAhit = 0
    teamBhit = 0
    n = int(input())
    potential_goalsA = n
    potential_goalsB = n
    shots = list(map(str, input()))
    for i in range(2*n):

        gerade = i%2
        if gerade == 0:
            teamAhit += int(shots[i])
            potential_goalsA -= 1
        else:
            teamBhit += int(shots[i])
            potential_goalsB -= 1
        if teamAhit > teamBhit + potential_goalsB:
           print(i +1)
           break;
        elif teamBhit > teamAhit + potential_goalsA:
            print(i +1)
            break;
        elif i == len(shots)-1:
            print(len(shots))
