# numbers_list = []
#
#
# def reverse():
#     for i in range(len(numbers_list)):
#         number = str(numbers_list[i])
#         new_number = number[::-1]
#         number = int(number)
#         new_number = int(new_number)
#         if new_number != number:
#             print(new_number)
#
#
# def user_input():
#     while True:
#         # num = int(input("How many times do you wanna reverse numbers?\n"))
#         num = int(input())
#         try:
#
#             #   print('Good choice\n')
#             break
#         except ValueError:
#             pass
#             # print('this is not a valid number, reconsider your choice')
#     return num
#
#
# def check_input():
#     reverse_number = user_input()
#     for i in range(reverse_number, 0, -1):
#
#         while True:
#             #inputed_number = input('Enter ' + str(i) + ' numbers more to reverse\n')
#             inputed_number = input()
#             try:
#                 val = int(inputed_number)
#                 #print('Good Choice')
#                 numbers_list.append(val)
#                 break
#             except ValueError:
#                 pass
#                 #print("Not a valid number, reconsider your choice")
#
#
# if __name__ == '__main__':
#     check_input()
#     reverse()


test_cases_count = int(input())

for i in range(test_cases_count):
    number = int(input())
    reversed_number = int(str(number)[::-1])
    print(reversed_number)