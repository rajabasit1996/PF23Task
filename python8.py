"""
Task 1
Using Nested for loop access each individual element from list with in
the list [[‘mehak’ ‘ayesha’ , ‘sadia’] [‘ali’ , ‘ahmed’ , ‘saif’ ]]


list = [["mehak", "ayesha" , "sadia"], ["ali", "ahmed" , "saif" ]]

for name in list:
    for k in name:
        print(k)


Task 2
Print the following pattern
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""


'''
rows = 6
row = 5

for i in range(0, rows):
    for j in range(0, i):
        print("*", end=' ')
    print("\r")
for k in range(row,0, -1):
    for c in range(0, k-1 ):
        print("*", end=' ')
    print("\r")
'''

"""
Modify your atm machine that you have designed earlier , you atm
machine has 4 different options
1) check balance
2) withdraw
3) deposit
4) exit Process your atm instructions until your user press an exit
button .

balance = 10000   # initial account balance

# Define the ATM functions
def check_balance():
    print("Your account balance is: ", balance)

def withdraw():
    amount = float(input("Enter amount to withdraw: "))
    balance = 10000
    if balance >= amount:
        balance -= amount
        print("Your new balance is: ", balance)
    else:
        print("Insufficient balance!")

def deposit():
    balance = 10000
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Your new balance is: ", balance)

# Start the ATM process
while True:
    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        check_balance()
    elif choice == 2:
        withdraw()
    elif choice == 3:
        deposit()
    elif choice == 4:
        print("Thank you for using our ATM!")
        break
    else:
        print("Invalid choice, please try again.")
"""

"""
Design a control applications for your home appliances, your task is to
control your room appliances like tv, fans , bulb lights.. If you press the
on button for your room's bulb it will turn on , if you press the off
button it will turn of, this system will constantly showing you options
for on and off your home appliances , once user press the exit button
then the program will be terminate.


# Define the appliance functions
def turn_on(appliance):
    if appliance["status"] == "off":
        appliance["status"] = "on"
        print(appliance["name"], "turned on.")
    else:
        print(appliance["name"], "is already on.")

def turn_off(appliance):
    if appliance["status"] == "on":
        appliance["status"] = "off"
        print(appliance["name"], "turned off.")
    else:
        print(appliance["name"], "is already off.")

# Define the appliances as dictionaries
tv = {"name": "TV", "status": "off"}
fan = {"name": "Fan", "status": "off"}
bulb = {"name": "Bulb", "status": "off"}

# Start the appliance control process
while True:
    print("\n1. Turn TV on")
    print("2. Turn fan on")
    print("3. Turn bulb on")
    print("4. Turn TV off")
    print("5. Turn fan off")
    print("6. Turn bulb off")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        turn_on(tv)
    elif choice == 2:
        turn_on(fan)
    elif choice == 3:
        turn_on(bulb)
    elif choice == 4:
        turn_off(tv)
    elif choice == 5:
        turn_off(fan)
    elif choice == 6:
        turn_off(bulb)
    elif choice == 7:
        print("Thank you for using our appliance control system!")
        break
    else:
        print("Invalid choice, please try again.") 
"""

"""
Task 5
Design a control mechanism of AC/Split for automatically adjust the AC
setting once the room temperature is so cold. Once the temperature of
room decreases to 15° then the compressor of AC switch off and when
the temperature is above 20° then automatically switch on the
compressor to obtain desired cool temperature. (Remember we dont
have sensor for getting the temperature of room just ask from the user
assume user as a thermostat) . This process will be continue while the
AC is on.

import time

def ac_control():
    compressor_on = False
    while True:
        temp = int(input("Enter the current room temperature in degrees Celsius: "))
        if temp <= 15 and compressor_on:
            print("Room temperature is too cold. Switching off compressor.")
            compressor_on = False
        elif temp >= 20 and not compressor_on:
            print("Room temperature is too hot. Switching on compressor.")
            compressor_on = True
        elif compressor_on:
            print("Room temperature is within desired range. Compressor is on.")
        else:
            print("Room temperature is within desired range. Compressor is off.")
        time.sleep(5)
ac_control() 
"""

"""
Design a program for creating a clock

import time

def get_current_time():
    #Returns the current time in HH:MM:SS format
    return time.strftime("%H:%M:%S")

def display_clock():
    #Displays the current time in a digital clock format
    while True:
        print("\r", get_current_time(), end="")
        time.sleep(1)

# Call the display_clock function to start the clock
display_clock()

"""
"""
Design a Calender system for 2023 in python , use strings methods for
creating a beautiful console. Align your text in a center position and
make some attractive borders using special characters.

# Define the year
year = 2023

# Define the months and their lengths
months = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

# Define the weekdays
weekdays = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

# Loop over the months
for month, days in months.items():
    # Print the month and year
    print(month.center(20, " "))
    print(str(year).center(20, " "))
    print("-" * 20)

    # Print the weekdays
    for day in weekdays:
        print(day, end="\t")
    print()

    # Print the days
    for day in range(1, days + 1):
        print(str(day).rjust(2), end="\t")

        # If this is the last day of the week, print a new line
        if (day + weekdays.index("Mo")) % 7 == 0:
            print()

    # Print a new line after each month
    print()
"""
"""
Design a console based application for Converting different currency.
You are required to ask user to choose input which currency you want
to convert and then ask the amount. After that ask in which currency
you want to convert. Then convert that currency into desired one...
(Currency should include Euro , Dollar, PkR, INR , and yen)

def convert_currency():
    currency_rates = {"EUR": 1.18, "USD": 1.0, "PKR": 0.0064, "INR": 0.014, "JPY": 0.0092}
    print("Which currency would you like to convert?")
    print("1. EUR\n2. USD\n3. PKR\n4. INR\n5. JPY")
    input_currency = input("Enter your choice (1-5): ")
    while input_currency not in ["1", "2", "3", "4", "5"]:
        input_currency = input("Invalid choice. Please enter a valid choice (1-5): ")
    input_currency = list(currency_rates.keys())[int(input_currency) - 1]
    print(f"\nYou selected {input_currency}\n")

    amount = float(input("Enter the amount you want to convert: "))

    print("Which currency do you want to convert to?")
    print("1. EUR\n2. USD\n3. PKR\n4. INR\n5. JPY")
    output_currency = input("Enter your choice (1-5): ")
    while output_currency not in ["1", "2", "3", "4", "5"]:
        output_currency = input("Invalid choice. Please enter a valid choice (1-5): ")
    output_currency = list(currency_rates.keys())[int(output_currency) - 1]
    print(f"\nYou selected {output_currency}\n")

    converted_amount = round(amount * currency_rates[input_currency] / currency_rates[output_currency], 2)
    print(f"\n{amount} {input_currency} is equivalent to {converted_amount} {output_currency}\n")
convert_currency()
"""

"""
#Create a mathematical functions
Prime function : for checking whether the number is prime or not
Even function : To check whether the number is even or not
Odd function : to check whether the number is odd or not
MixNumber : To tell the about all the properties of number ( even or
odd, positive or negative integer and prime number)
If user gives MixNumber( 2 ) then the output will be 2 is also prime
number , 2 is also an odd , and 2 is prime also.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 == 1

def mix_number(num):
    properties = []
    if is_even(num):
        properties.append("even")
    else:
        properties.append("odd")
    if num > 0:
        properties.append("positive")
    elif num < 0:
        properties.append("negative")
    if is_prime(num):
        properties.append("prime")
    return " ".join([str(num), "is also", " ".join(properties), "number."])

num = int(input("Enter Any number: "))

if is_prime(num):
    print(num, "is prime.")
else:
    print(num, "is not prime.")

if is_even(num):
    print(num, "is even.")
else:
    print(num, "is not even.")

if is_odd(num):
    print(num, "is odd.")
else:
    print(num, "is not odd.")

print(mix_number(num)) 
"""

"""
#Create a function that helps to solve the quadratic equation

def solve_quadratic_eq(a, b, c):
    
    #Solves a quadratic equation of the form ax^2 + bx + c = 0 for x.
    #Returns a tuple containing the two possible values of x.
    
    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c

    # If the discriminant is negative, the equation has no real solutions
    if discriminant < 0:
        return None

    # If the discriminant is zero, the equation has one real solution
    elif discriminant == 0:
        x = -b / (2 * a)
        return (x,)

    # If the discriminant is positive, the equation has two real solutions
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return (x1, x2)
# Solve x^2 + 5x + 6 = 0 for x
solutions = solve_quadratic_eq(1, 5, 6)
print(solutions)  # Output: (-2.0, -3.0)
"""

"""
Create a function that helps to solve the linear equation

def solve_linear_eq(a, b, c):
    #    Solves a linear equation of the form ax + b = c for x.
    # Returns the value of x.
    
    x = (c - b) / a
    return x
# Solve 3x + 5 = 14 for x
x = solve_linear_eq(3, 5, 14)
print(x)  # Output: 3.0 
"""

"""
#Create a function that calculates the radius and diameter of circle.

def circle(circumference):
    radius = circumference / 6.28
    diameter = radius * 2

    return radius, diameter

r, d = circle(88)
print("Radius:", r)
print("Diameter:", d) 
"""
