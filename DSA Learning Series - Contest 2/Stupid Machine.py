t = int(input())

for i in range(t):
    n = int(input())

    tokens = list(map(int, input().split()))
    maximum = 0
    max_tokens = float('inf')
    for i in range(n):

        max_tokens = min(max_tokens, tokens[i])
        maximum += max_tokens
    print(maximum)
