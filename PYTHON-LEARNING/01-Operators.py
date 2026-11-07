# Challenge 01

a = 25
b = 7
c = 3

result = a + b * c - 10
print(result)

#  a + b * c - 10
#  a + ( b * c ) - 10
#  25 + ( 7 * 3 ) - 10
#  25 +  21 - 10
#  46 - 10
#  36 //

# Challenge 02

x = 100
y = 9

result = (x // y) + (x % y) * 5
print(result)

# 100 // 9 = 11 
# 100 % 9 = 1
# 11 + 1 * 5
# 11 + 5
#  16

# Challenge 03

a = 2
b = 3
c = 4

result = a ** b + c ** 2 - 10
print(result)

# 2 ** 3 = 8
# 4 ** 2 = 16
# 8 + 16 - 10
# 24 - 10
# 14 //

# Challenge 04

a = 17
b = 5
c = 3
d = 2

result = ((a + b) * c ** d - a // b) % (b + d)
print(result)

# (17 + 5) = 22
# 3 ** 2 = 9
# 17 // 5 = 3
# ( 5 + 2) = 7

# 22 * 9 - 3 % 7
# 198 - 3 % 7
# 195 % 7 
# 6