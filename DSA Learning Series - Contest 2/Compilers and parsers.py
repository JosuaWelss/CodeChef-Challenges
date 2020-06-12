for i in range(int(input())):
    klammern = input()
    stack = []
    index = 0
    for i in range(len(klammern)):
        if klammern[i] == '<':
            stack.append('<')
        else:
            if len(stack) == 0:
                break
            else:
                stack.pop()
                if len(stack) == 0:
                    index = i+1
    print(index)
#
# ## alternative????
# for i in range(int(input())):
#     klammern = input()
#     öffnungen = []
#     schliessungen_to_come = []
#     for i in range(len(klammern)):
#         if klammern[i] == '<':
#             öffnungen.append('<')
#         else:
#             schliessungen_to_come.append('>')
#         ## if len(öffnungen) < len(schliessungen_to_come):
#             print(i)
#             break
#
#         if i == len(klammern)-1:
#             print(len(klammern))
