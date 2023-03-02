'''
Create a password based system for a mobile. Set the password as “PF-
23” if user enter the correct password then display this message

You are successfully login. Otherwise display this message : You entered
a wrong Password.
'''

#passw = "PF-23"
#pw = input("Enter Your Password ")
#if pw == passw:
#    print("You are successfully login!")
#else:
#    print("You entered a wrong Password")

'''
Create a Login Form.
Ask user to enter his mobile number and password
Set the mobile# as “03073514050” and password as “PF-23” if user
enter the correct password then display this message
You are successfully login. Otherwise display this message :
You entered a wrong Email or Password..
'''
#num = "03073514050"
#passw = "PF-23"

#cell = input('Enter your mobile num ')
#pas = input("Enter Password ")

#if cell == num and pas == passw:
#    print("You are successfully login ")
#else:
#    print("You entered a wrong Email or Password")

'''
Write a program to take input marks of five subjects from user
Python, Java, C++, Mathematics and DSA. Calculate percentage and
grade according to following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F

python = int(input("Enter your marks in PYTHON: "))
java = int(input("Enter your marks in JAVA: "))
c = int(input("Enter your marks in C++: "))
maths = int(input("Enter your marks in Mathematics: "))
ds = int(input("Enter your marks in DSA: "))

marks = python + java + c + maths + ds
percentage = (marks/500) * 100

if percentage >= 90:
    print("Grade A")
elif percentage>=70:
    print("Grade C")
elif percentage>=60:
    print("Grade D")
elif percentage>=50:
    print("Grade E")
elif percentage>=40:
    print("Grade E+")
else:
    print("Grade F")
'''

#write a program to take any alphabet as input and check whether it is vowel or consonant
'''vowels = ['a','e','i','o','u', 'A','E','I','O','U']

alpha = input("Enter any alphabet ")

if alpha in vowels:
    print("Vowel")
else:
    print('Consonant')
'''

'''
Write a program to check whether the triangle is equilateral, isosceles
or scalene triangle. (study about how to check whether the triangle is
equilateral etc and apply conditional statements by taking the
sides/angles from user)





x = int(input('Enter value of first side: '))
y = int(input('Enter value of first side: '))
z = int(input('Enter value of first side: '))
# _Check for equilateral triangle
if x == y == z:
    print("Equilateral Triangle")
    
# _Check for Isosceles triangle
elif x == y or y == z or z == x:
    print("Isosceles Triangle")
    
# _Check for Scalene triangle
else:
    print("Scalene Triangle")

'''
'''
Create a registration form that receive information related to user
name, email, password , age and gender.
If the user age is greater than 13 create its Account else just say that
you are not eligible to Create an ID on this platform. Try after ___ years
( In ___ years place the age of remaining years left when he turns out to
be 13 )
'''
'''
name = input("Enter your Name: ")
email = input("Enter your Email: ")
passw = input("Enter your Password: ")
age = int(input("Enter your Age: "))
Gender = input("Enter your Gender: ")

age1  = 13 - age
if age >= 13:
    print("Account Creation Successful")
else:
    print("You are not eligible to create an ID on this platform. Try after", age1,"Years")
'''
'''
Design a console based application for Converting different currency.
You are required to ask user to choose input which currency you want
to convert and then ask the amount. After that ask in which currency
you want to convert. Then convert that currency into desired one...
(Currency should include Euro , Dollar, PkR, INR , and yen)


currency = input("Which currency you want to convert ")
amount = int(input("Amount you want to convert "))
c_currency = input("In which currency you want to convert ")

if currency == "Pkr" and c_currency == "Euro":
    eur = amount / 284
    print("€",eur)
elif currency == "Pkr" and c_currency == "Dollar":
     dollar = amount / 278
     print("$",dollar)
elif currency == "Pkr" and c_currency == "Pkr":
     pkr = amount * 1
     print("Rs.",pkr)
elif currency == "Pkr" and c_currency == "Pkr":
     inr = amount / 3.18
     print("₹",inr)
elif currency == "Pkr" and c_currency == "Yen":
     yen = amount / 3.18
     print("¥",yen)

elif currency == "Inr" and c_currency == "Euro":
     euro = amount * 0.011
     print("€",euro)
elif currency == "Inr" and c_currency == "Dollar":
     dollar = amount * 0.012
     print("$",dollar)
elif currency == "Inr" and c_currency == "Pkr":
     pkr = amount * 3.24
     print("Rs.",pkr)
elif currency == "Inr" and c_currency == "Inr":
     inr = amount * 1
     print("₹",inr)
elif currency == "Inr" and c_currency == "Yen":
     yen = amount * 1.65
     print("¥",yen)

elif currency == "Euro" and c_currency == "Euro":
     euro = amount * 1
     print("€",euro)
elif currency == "Euro" and c_currency == "Dollar":
     dollar = amount / 1.06
     print("$",dollar)
elif currency == "Euro" and c_currency == "Pkr":
     pkr = amount * 284.16
     print("Rs.",pkr)
elif currency == "Euro" and c_currency == "Inr":
     inr = amount * 87.85
     print("₹",inr)
elif currency == "Euro" and c_currency == "Yen":
     yen = amount * 144.99
     print("¥",yen)

elif currency == "Dollar" and c_currency == "Euro":
     euro = amount * 0.94
     print("€",euro)
elif currency == "Dollar" and c_currency == "Dollar":
     dollar = amount * 1
     print("$",dollar)
elif currency == "Dollar" and c_currency == "Pkr":
     pkr = amount * 267.67
     print("Rs.",pkr)
elif currency == "Dollar" and c_currency == "Inr":
     inr = amount * 82.56
     print("₹",inr)
elif currency == "Dollar" and c_currency == "Yen":
     yen = amount * 144.99
     print("¥",yen)

elif currency == "Yen" and c_currency == "Euro":
     euro = amount * 0.0069
     print("€",euro)
elif currency == "Yen" and c_currency == "Dollar":
     dollar = amount * 0.0073
     print("$",dollar)
elif currency == "Yen" and c_currency == "Pkr":
     pkr = amount * 1.96
     print("Rs.",pkr)
elif currency == "Yen" and c_currency == "Inr":
     inr = amount * 0.61 
     print("₹",inr)
elif currency == "Yen" and c_currency == "Yen":
     yen = amount * 1
     print("¥",yen)
'''

'''
Design an ATM machine that has 3 main features
1) Deposit
2) Withdraw
3) Check balance
Current balance is 5000, If the withdraw balance is equal or less than
5000 then cash out the desired withdraw amount. If it exceed from
current balance then deliver a message that you dont have enough
balance. When user select an option "1" then update the current
balance. If user choose an option, "3" then show them their current
balance


c_balance = 5000
withdraw = int(input("Enter Amount "))


if withdraw <= c_balance:
    print("Transaction Successful")
elif withdraw >= c_balance:
    print("You dont have enough balance")

option = int(input("select option 1 or 3 "))

if option == 1:
    print('Current balance updated successfully!')
elif option == 3:
    print(c_balance)

'''

'''
GameXone offering a new position in their software house, you are
selected for an interview. The criteria for selecting your position either
as a programmer or management person is that if you are having 4-5
years of experience in game development than you will be hired as a
Developer otherwise they will shortlist your for management.
'''
'''
yoe = int(input("Enter your Experience as a developer "))

if yoe < 4:
    print("You are shortlisted as a managerial staff")
else:
    print("You're selected as Programer")
'''

'''
Design a career counseling system for students to select their field. You
are requested to think like a counsellor who guide students to choose a
career according to their interest and passion. If their hobbies , or
interest is in arts, drawing , management , suggest them a field of Arts ,
if they are logical, having expertise and interest in programming ,
problem solving ,technologies than suggest to pursue their career in
Engineering domain . If they showed their interest in bio , science ,
discipline and development of humanity than suggest them a medical
field.
'''
'''
field = input("Enter your Field ")
list = ['Arts', "Drawing" , "Management"]
prog = ['Logical', 'Programming', 'Problem Solving', "Technical"]
sci = ["Bio", "Science", "Discipline", "Development of humanity"]

if field in list:
    print("Field of Arts is best suited for you")
elif field in prog:
    print("Engineering domain is best suited for you")
elif field in sci:
    print("Medical Field is best suited for you")

'''











