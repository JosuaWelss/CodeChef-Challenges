t = int(input())

for i in range(t):
    n = int(input())
    profit = 0;
    for j in range(n):
        s, p, v = map(int, input().split())
        people = p//(s+1)
        max = people * v
        if max > profit:
            profit = max
    print(profit)