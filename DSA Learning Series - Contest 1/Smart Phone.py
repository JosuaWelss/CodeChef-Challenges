customer_budget = []
number_of_customers = int(input())
for i in range(number_of_customers):
    customer_budget.append(int(input()))
bestprice = 0

customer_budget.sort()
for i in range(number_of_customers):
    temp_price = customer_budget[i]
    highest_price = temp_price * (number_of_customers-i)
    if bestprice < highest_price:
        bestprice = highest_price
print(bestprice)



# alternative:
# cook your dish here
# n=int(input())
# a=[]
# for i in range(n):
#     a.append(int(input()))
# a.sort()
# m=0
# #print(a)
# for i in range(n):
#     if a[i]*(n-i) >m:
#         m=a[i]*(n-i)
#         #print(m,a[i])
#
# print(m)