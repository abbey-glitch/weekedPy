# nums = [1, 2, 3, 4, 5]
# for num in range(0, 10, 2):
#     print(num)
#     # if(num == 1):
#     #     print(f"this is {num}")
#     print(num)
# for num in nums:
#     print(num)

# prime_num = []
# for num in range(0, 10):
#     if(num > 1):
#        print(f"this is the parent loop {num}")
#        for number in range(2, num):
#             if(num%number)== 0:
#             #    print(f"this is even: {number}")
#                break
#        else:
#           prime_num.append(num)
#           print(prime_num)


# list itemd and it methods
fruits = ['orange', 'banana', 'apple', 'mango']
# append it add to the last list item
# add = fruits.append('lemon')
# pop method in a list item remove the last item in a list and also takes the index of the params to be removed
# fruits.pop()
# fruits.clear()
fruits.insert(4, 'pawpaw')
fruits[2] = 'citrus'
# fruits.insert(2, 'berry')
# box = ['apple']
# box.extend(fruits)
# print(box, fruits)
sample = []
fruits.copy()
print(sample);