#
# #slow solution
#
# number_of_inputs = int(input())
#
# for i in range(number_of_inputs):
#     number_to_compute= int(input())
#     factorial = 1
#
#     for i in range (1, number_to_compute+1):
#         factorial *= i
#     print(factorial)
#     reversed_factorial = int(str(factorial)[::-1])
#     number_of_zeros = len(str(factorial)) - len((str(reversed_factorial)))
#
#     print(number_of_zeros)
#
#


def count (x):
    i = 5
    zeros = 0
    while x >= i:
        zeros += x // i
        i *= 5
    return zeros


number_of_inputs = int(input())


for i in range(number_of_inputs):
    number_to_compute = int(input())
    print(count(number_to_compute))