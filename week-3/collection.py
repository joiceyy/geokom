var_a = [ 'a', 'b', 'c', 'd', 'e', 'f']

# list
print('**********list**********')
print(var_a[0])
print(var_a[-6])
print('------------')

# slice
print('**********slice**********')
print(var_a[-1:])
print('------------')

# stride
print('**********stride**********')
# print(var_a[0:6:3])
# print(var_a[1:6:2])
# print(var_a[0:6:5])
print(var_a[0:2:1] + var_a[3:5:1])
print('------------')


# practice
print('**********practice**********')
var_b = [8, 2, 3, 1, 2, 4, 5]
print('------------')

# 1. Syntax to get the value of 1 from var_b: 
print('**********Syntax to get the value of 1 from var_b**********')
print(var_b[3])
print('------------')

# 2. Syntax to get the value of [1,2,4] from var_b:
print('**********Syntax to get the value of [1,2,4] from var_b**********')
print(var_b[3:6])
print('------------')


# 3. Syntax to get the value of [8,1,5] from var_b:
print('**********Syntax to get the value of [8,1,5] from var_b**********')
print(var_b[0:7:3])
print('------------')

# To get length of list
print('**********To get length of list**********')
print(len(var_b))
print('------------')

# To append new data to list
print('**********To append new data to list**********')
var_b = [8, 2, 3, 1, 2, 4, 5]
var_b.append(20)
print(var_b)
print('------------')

# To insert new data to list
print('**********To insert new data to list**********')
var_b = [8, 2, 3, 1, 2, 4, 5]
var_b.insert(3, 20)
print(var_b)
print('------------')


# pop value
print('**********pop value**********')
var_b = [8, 2, 3, 1, 2, 4, 5]
var_b.pop(5)
print(var_b)
print('------------')


# remove 
print('**********remove**********')
var_b = [8, 2, 3, 1, 2, 4, 5]
var_b.remove(2)
print(var_b)
print('------------')

# statiscall analysis
print('**********statiscall analysis**********')
var_b = [8, 2, 3, 1, 2, 4, 5]
print(min(var_b))
print(max(var_b))
print('------------')

# Replacing / update list value
print('**********Replacing / update list value**********')
var_b = [8, 2, 3, 1, 2, 4, 5]
var_b[3] = 7
print(var_b)
print('___________________&________________________')

var_b[0:5] = [5]
print(var_b)
print('------------')

# 2d list
# list in list = row then coloum
print('**********LIST IN LIST**********')
var_b = [[ 8, 2, 3, 1, 2, 4, 5], 
         [18, 12, 13, 11, 12, 14, 15],
         [28, 22, 23, 21, 22, 24, 25],
         [38, 32, 33, 31, 32, 34, 35]]
print(var_b[2][3])
print('__________________&______________________')

var_c = [[14,26,29,12,17],
         [4,4,4,8,10],
         [2003,2005,2007,2009,2010],
         ['anak 1', 'anak 2', 'anak 3', 'anak 4', 'anak 5']]
print(var_c[1][4] , var_c[2][3])
print('------------')

# list operation
print('**********list operation**********')
print('firts : addition with +')
var_b = [8, 2, 3, 1, 2, 4, 5,7,24,89,45,5]
var_c = [18, 12, 13, 11, 12, 14, 15,11,26]
print(var_c + var_b)
print('____________________________________________')

print('Scalar Multiplication * with int')
print(var_c * 3)
print('_____________________________________________')


# tuples
print('**********Tuples**********')




