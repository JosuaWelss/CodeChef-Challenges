# ##inefficient solution
#
# test_cases = int(input())
# INQ_List = []
# coin_list = []
#
#
# def count_coins(q):
#     counter = 0
#     if q == 1:
#         for i in range(len(coin_list)):
#             if (coin_list[i] == 'H'):
#                 counter += 1
#     else:
#         for i in range(len(coin_list)):
#             if (coin_list[i] == 'T'):
#                 counter += 1
#     return counter
#
#
# def change(k, coinlist1):
#     for i in range(k + 1):
#
#         if coinlist1[i] == 'H':
#             coinlist1[i] = 'T'
#         else:
#             coinlist1[i] = 'H'
#
#
# for i in range(test_cases):
#     number_of_games_played = int(input())
#     for j in range(number_of_games_played):
#         INQ_List = list(map(int,input().split()))  ## I = Initial state of coins(1 = all head, 2 = all tail), N = Number of rounds, Q = 1 or 2( 1 = guess number of heads at the end of game 2 n= number of tails)
#         if INQ_List[0] == 1:
#             for k in range(int(INQ_List[1])):
#                 coin_list.append('H')
#
#         else:
#             for k in range(int(INQ_List[1])):
#                 coin_list.append('T')
#
#         for i in range(len(coin_list)):
#             change(i, coin_list)
#
#         print(coin_list)
#         real_counter = count_coins(INQ_List[2])
#         print(real_counter)
#         coin_list.clear()


testcases = int(input())
h = 0
t = 0
for j in range(testcases):
    games = int(input())
    for k in range(games):
        i, n, q = (map(int, input().split()))## I = Initial state of coins(1 = all head, 2 = all tail), N = Number of rounds, Q = 1 or 2( 1 = guess number of heads at the end of game 2 n= number of tails)
        if i == 1:
            h = n//2
            t = n-h
        else:
            t = n//2
            h = n-t
        if q == 1:
            print(h)
        else:
            print(t)
