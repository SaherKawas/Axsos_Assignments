#1
def a():
    return 5
print(a())
#my prediction is 5

#2
def a():
    return 5
print(a()+a())
#my prediction is 10

#3
def a():
    return 5
    return 10
print(a())
# my prediction is 5

#4
def a():
    return 5
    print(10)
print(a())
#my prediction is 5

#5
def a():
    print(5)
    return 8
x = a()
print(x)
#my prediction is: the first print is 5 (didn't know the second print)
# print("**********************")
# #6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))
# # my prediction is 8

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# my prediction is 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a()) 
# my prediction is 100, 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# my prdeiction is 7, 14, 21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
#my prediction is 8 
# print("**********************")

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
# my prediction is 500, 300, 
# print("**********************")
# print("**********************")

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
#my prediction is 500,300,500,500
# print("**********************")
# print("**********************")
#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
#my prediction is 500, 300, 500, 300
print("**********************")
# 14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# my prediction is 1, 2, 3
print("**********************")
#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y) 
#my prediction is 1, 10, 3, 5