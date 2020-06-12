
## Solution 1, works only for inputs with one integer at a time

# number_of_tests = int(input())
#
# number_of_cars_passing_with_max_speed = 0
# car_in_front_speed = 0
# highspeed_of_cars = 0
#
#
# for i in range(number_of_tests):
#     number_of_cars = int(input())
#     for j in range(number_of_cars):
#             car_max_speed = int(input())
#         if j == 0:
#             number_of_cars_passing_with_max_speed += 1
#             car_in_front_speed = 0
#         if car_max_speed < car_in_front_speed:
#             number_of_cars_passing_with_max_speed += 1
#         car_in_front_speed = car_max_speed
#     print(number_of_cars_passing_with_max_speed)
#     number_of_cars_passing_with_max_speed = 0



## Solution 2


# number_of_test = int(input())
# for i in range(number_of_test):
#     number_of_cars = int(input())
#     inputs = list(map(int, input().split()))
#     number_of_cars_passing_with_max_speed = 1
#     for j in range(1, number_of_cars):
#         car_in_front_speed = inputs[j - 1]
#         car_max_speed = inputs[j]
#         if car_max_speed <= car_in_front_speed:
#             number_of_cars_passing_with_max_speed += 1
#         else:
#             car_max_speed = car_in_front_speed                      ----!!!! variable changes but not the list entry
#     print(number_of_cars_passing_with_max_speed)

number_of_test = int(input())
for i in range(number_of_test):
    number_of_cars = int(input())
    inputs = list(map(int, input().split()))
    number_of_cars_passing_with_max_speed = 1
    for j in range(1, number_of_cars):
        if inputs[j] <= inputs[j - 1]:
            number_of_cars_passing_with_max_speed += 1
        else:
            inputs[j] = inputs[j - 1]
    print(number_of_cars_passing_with_max_speed)
