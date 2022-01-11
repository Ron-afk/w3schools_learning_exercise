# if 5 > 2:
#     print("yeah!")
#
#
# x = 5
# y = "Hello, World!"
#
# print(y)

# x = "awsome"
#
# def myfunc():
#     x = "fantastic"
#     print("Python is " + x)
#
# myfunc()
#
# print("Python is " + x)

# def myfunc():
#   global x
#   x = "fantastic"
#
# myfunc()
#
# print("Python is " + x)
#
# print(type(x))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

txt = "The best things in life are free!"
print("free" in txt)

a = "Hello, World!"
print(a.split(","))

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

age,year = 36,1980
text = "I am {}, and born in {}"
print(text.format(age,year))

print(10 > 9)
print(10 == 9)
print(10 < 9)

print(bool("Hello"))
print(bool(15))
print(bool([]))

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thistuple = ("apple", "banana", "cherry")
print(thistuple)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)