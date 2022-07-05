# name = 'Rishabh'
# print(name[::-3])


# ---------------------------------------------------------------------------------------------------


# # Leap Year

# def is_leap(year):
#     leap = False
    
#     # Write your logic here
#     if year%4 == 0:
#         if year%100 == 0:
#             if year%400 == 0:
#                 leap = True
#             else:
#                 leap = False
#         else:
#             leap=True
#     return leap

# year = int(input('Enter a year : '))
# print(is_leap(year))


# ---------------------------------------------------------------------------------------------------


# if __name__ == '__main__':
#     n = int(input("Enter a number : "))
#     n_list = []
#     for i in range(1, n+1):
#         n_list.append(f'{i}')

#     print(''.join(n_list))


# ---------------------------------------------------------------------------------------------------


# import numpy

# my_array = numpy.array([ [3, 4], [7, 8] ])

# sum = numpy.array(numpy.sum(my_array, axis = 0))
# print (sum)
# print (numpy.prod(sum, axis = 0))    


# ---------------------------------------------------------------------------------------------------


# if __name__ == '__main__':
#     n = int(input().strip())
#     if n%2 != 0:
#         print("Wierd")
#     elif n%2 == 0 and 2<=n<=5:
#         print("Not Wierd")
#     elif n%2 == 0 and 6<=n<=20:
#         print("Wierd")
#     elif n%2 == 0 and n>=20:
#         print("Not Wierd")
#     else:
#         pass


# ---------------------------------------------------------------------------------------------------


# # Given sets of integers, and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either or but do not exist in both.
# set_a = set()
# set_b = set()
# set_c = set()

# set_size_a = int(input())
# elements_a = str(input())
# list_a = elements_a.split()

# for i in range(0, set_size_a):
#     set_a.add(int(list_a[i]))
# print(set_a)


# set_size_b = int(input())
# elements_b = str(input())
# list_b = elements_b.split(" ")

# for j in  range(0, set_size_b):
#     set_b.add(int(list_b[j]))
# print(set_b)

# set_c.update(set_a.difference(set_b))
# set_c.update(set_b.difference(set_a))
# print(set_c)
# order_list = []
# for k in set_c:
#     order_list.append(k)

# order_list.sort()

# for l in order_list:
#     print(l)


# ---------------------------------------------------------------------------------------------------


# You are given three integers and representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by i j k on a 3D grid where the sum of i j k is not equal to n. Please use list comprehensions rather than multiple loops, as a learning exercise. 

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    cube_coordinates = [[i] for i in range(0, x+1)]
    cube_coordinates = [[j] for i in range(0, x+1)]
    cube_coordinates = [[j] for i in range(0, x+1)]
    print(cube_coordinates)

