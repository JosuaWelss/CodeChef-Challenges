testcases = int(input())
number = []
for i in range(testcases):
    k, d0, d1 = map(int, input().split())

    result = d0 + d1

    d2 = (result) % 10

    if k > 0:
        result += d2
        k -= 1


    next_four_num = ((2*result)% 10 + (4*result)%10 + (8*result)%10 + (6*result)%10)

    temp = next_four_num * ((k-3)/4)