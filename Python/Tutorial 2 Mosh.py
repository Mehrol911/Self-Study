#Arithmetic operations
print(10 ** 3) #we get integer   + - / //=integer *  **=power
x = 10
x = x+3
x += 3 #augmented assignment operator increment
print(x)  

#Operator Precedence
x = (10 + 3) * 2 ** 2
print(x)  #exponentiton, * or /, then + or -
x = (2 + 3) * 10 - 3

#Math Functions
import math #math module
x = 2.501
print(round(x))
print(abs(-2.9))

#If statements
is_hot = True
is_cold = False
if is_hot: 
   print("It's a hot day")  #shift + tab -> boshiga
   print("Drink plenty of water")
elif is_cold:
    print("It is a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

#exercise 
price = 1000000
has_good_credit = False
if has_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f"Down payment: ${down_payment}")
 

#Logical operators  01:06:32
has_high_income = True   # and = 1,1   # or = 0,1
has_good_credit = False 
if has_high_income and has_good_credit:
    print("Eligible for Loan")

has_good_credit = True
has_criminal_record = True 
if has_high_income and not has_criminal_record:
    print("Eligible for Loan")
 
#comparison operators 01:11:25 
temperature = 25
if temperature > 30: #>=, ==, =<, <, >, !=
    print("It's a hot day")
else: 
    print("It's not a hot day")

#exercise
name = input("Write your name: ")
length = (len(name))
if length < 3:
   print("Name must be at least 3 characters")
elif length > 50:
    print("Name can be maximum of 50 characters")
else:
    print("Name looks good")   
