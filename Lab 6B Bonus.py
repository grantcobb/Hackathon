# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# UIN:          528000393
# Name: 		Alex Tung
# Section:		552
# Assignment:	Lab 6B Bonus (e.g. Lab 1b-2)
# Date:		04 10 2019

in1 = int(input("Input a positive integer: "))
x = 0
for i in range(in1+1):
    x += i
    print("The sum from 0 to", i, "equals", x)
print("________________________________")

b = 0
y = 0
while b in range(in1+1):
    y += b
    b += 1
    print("The sum from 0 to", b-1, "equals", y)
print("________________________________")

p = 1
for k in range(1, in1+1):
    p *= k
    print("The product from 1 to", k, "equals", p)
print("________________________________")

b2 = 1
y2 = 1
while b2 in range(1, in1 + 1):
    y2 *= b2
    b2 += 1
    print("The product from 1 to", b2-1, "equals", y2)
print("________________________________")