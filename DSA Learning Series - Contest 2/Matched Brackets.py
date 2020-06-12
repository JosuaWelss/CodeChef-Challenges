## 1 = (
## 2 = )

length = int(input())
brackets = list(map(int, input().split())) ## brackets = [int(i) for i in input().split]

stack = []
max_depth = 0
max_stacklength = 0
symbols_between_brackets = 0
max_symbols_between_brackets = 0
position_of_max_symbols_between_brackets = 0
first_position_of_max_depth = 0

counter = 0
max_counter = 0

for i in range(length):
    if brackets[i] == 1:
        stack.append('X')

        if max_stacklength < len(stack):
            first_position_of_max_depth = i + 1
            max_stacklength = len(stack)
            max_depth = len(stack)

    elif 'X' in stack:
        symbols_between_brackets += 2
        stack.pop()
        if len(stack) == 0:
            if max_symbols_between_brackets < symbols_between_brackets:
                max_symbols_between_brackets = symbols_between_brackets
                position_of_max_symbols_between_brackets = i - max_symbols_between_brackets + 2
            symbols_between_brackets = 0

print('%d %d %d %d' % (max_depth, first_position_of_max_depth, max_symbols_between_brackets, position_of_max_symbols_between_brackets))


### shit der die lösung verkackt hat:
        # popping += 1

    #
    # if max_depth < popping:
    #     max_depth = popping
