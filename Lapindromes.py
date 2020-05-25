# from collections import Counter
#
# inputNumber = int(input())
#
# for i in range(inputNumber):
#     word = input()
#     if len(word) % 2 == 0:
#         word1 = word[:len(word) // 2]
#         word2 = word[len(word) // 2:]
#
#     else:
#         word1 = word[:len(word) // 2]
#         word2 = word[len(word) // 2 + 1:]
#
#     if Counter(word1) - Counter(word2) != Counter():
#         print('NO')
#     else:
#         print('YES')
#

n = int(input())
for i in range(n):
    word = list(input())
    if len(word) % 2 == 0:
        word1 = word[:len(word) // 2]
        word2 = word[len(word) // 2:]

    else:
        word1 = word[:len(word) // 2]
        word2 = word[len(word) // 2 + 1:]

    word1.sort()
    word2.sort()

    if word1 == word2:
        print('YES')
    else:
        print('NO')
