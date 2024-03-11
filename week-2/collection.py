var_a = [ 'a', 'b', 'c', 'd', 'e', 'f']

# list
print(var_a[0])
print(var_a[-6])

# slice
print(var_a[-1:])

# stride
# print(var_a[0:6:3])
# print(var_a[1:6:2])
# print(var_a[0:6:5])
print(var_a[0:2:1] + var_a[3:5:1])



# practice
var_b = [8, 2, 3, 1, 2, 4, 5]

# 1. Syntax to get the value of 1 from var_b: 
print(var_b[3])

# 2. Syntax to get the value of [1,2,4] from var_b:
print(var_b[3:6])

# 3. Syntax to get the value of [8,1,5] from var_b:
print(var_b[0:7:3])

# To get length of list
print(len(var_b))

# To append new data to list
var_b = [8, 2, 3, 1, 2, 4, 5]
var_b.append(20)
print(var_b)

# To insert new data to list
var_b = [8, 2, 3, 1, 2, 4, 5]
var_b.insert(3, 20)
print(var_b)


# pop value
var_b = [8, 2, 3, 1, 2, 4, 5]
var_b.pop(5)
print(var_b)

# remove value
var_b = [8, 2, 3, 1, 2, 4, 5]
var_b.remove(2)
print(var_b)

# statiscall analysis
var_b = [8, 2, 3, 1, 2, 4, 5]
print(min(var_b))
print(max(var_b))

# Replacing / update list value
var_b = [8, 2, 3, 1, 2, 4, 5]
var_b[3] = 7
print(var_b)

var_b[0:5] = [5]
print(var_b)