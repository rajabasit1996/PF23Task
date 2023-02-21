#1 Design a calculator that takes 2 values from user to apply mathematical operations Addition, subtraction, and division, multiplication, floor division.

#a = int(input("Enter first value "))
#b = int(input("Enter second value "))
'''
c = a + b
d = a - b
e = a / b
f = a * b
g = a // b

print('Sum of two numbers is', c,'\n','Subtraction of two numbers is', d,'\n','Division of two numbers is', e,
      '\n','Multiplication of two numbers is', f,'\n',"Floor division of two numbers is: ", g)
'''
#Takes 2 arguments from user and check whether they are equal or not
'''
c = a == b
print(c) 
'''
#Design a system that calculates the area of a plot.

'''
area_of_plot = a * b
print("Area of plot is: ",area_of_plot, "sq ft")
'''

#Design a BMI system both in (US and Metric unit)
'''
a = float(input("Enter your height in meters: "))
b = int(input("Enter your weight in Kg: "))

bmi =b / (a*a)

print('Your BMI is: ',bmi)
'''

#Other way
'''
a = float(input("Enter your height in centimeters: "))
b = float(input("Enter your weight in Kg: "))

bmi = (b/a/a) * 10000
print(bmi)
'''
'''
Create a program that convert –
 User weight in kG into pounds , and
 height into inches
 Radian to degree
'''
#weight = float(input("Enter your weight in Kg: "))
#height = float(input("Enter your height in ft: "))
#pounds = weight * 2.202

#conv = height *12
#print("Your height in Inches : ", conv)
#print('Your weight in Pounds is: ', pounds)

#radian = int(input("Enter angles in Radian "))

#degrees = radian * 180 / 3.14

#print("Degress = ", degrees)

'''
Write a Python program to calculate the –
 Area of a trapezoid –
'''
#base1 = float(input("Enter value for first base: "))
#base2 = float(input("Enter value for second base: "))
#height = float(input("Enter value for height: "))

#base = base1 + base2

#trapezoid = (base / 2) * height

#print("Area of trapezoid = ",trapezoid)

#Area of a parallelogram
#base = float(input("Enter value for first base: "))
#height = float(input("Enter value for height: "))

#area = base * height

#print("Area of parallelogram = ",area)

#Calculate surface volume and area of a cylinder.

#A cylinder's volume is π r² h, and its surface area is 2π r h + 2π r².
#Volume of a cylinder

radius = float(input("Enter value for radius: "))
height = float(input("Enter value for height: "))

#vol = 3.14 * (radius*radius) * height

#print('Approximate value for volume of cylinder is: ',vol)

#Surface area of cylinder

surface = 6.28 * radius * height + 6.28 * (radius*radius)
print('Approximate value for volume of cylinder is: ', surface)
