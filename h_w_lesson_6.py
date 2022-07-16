#task_1 The greatest number. Write a Python program to get the largest number from a list of random numbers
# with the length of 10

# import random
#
# numbers = (random.sample(range(1,100),10))
# print(numbers)
# print ('Max element in the row above is:', max(numbers))


# #task_2 Exclusive common numbers: Generate 2 lists with the length of 10 with random integers from 1 to 10
# # and make a third list containing the common integers between the 2 initial lists without any duplicates.
#
# import random
#
# list_1 = (random.sample(range(1,11),5))
# print(list_1)
# list_2 = (random.sample(range(1,11),5))
# print (list_2)
# list_3 = list(set(list_1+list_2))
# print(list_3)
# #
#
# #task_3 Extracting numbers, Make a list that contains all integers from 1 to 100, then find all integers
# # from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list.
# # Finally, print the list.

# main_list = (list(range(1,100)))
# print(main_list)
#
# a=0
# b=0
# while a<99:
#     a+=1
#     b+=1
#     if b//7==b/7 and b % 5 !=0:
#         print (list([b]))
