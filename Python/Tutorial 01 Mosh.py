#Python Tutorial - with Mosh
print("Mekhrol Bazarov")
print('*' * 10)     #10 times *

#-----------------------------------------------------------------------

#variables  00:13:03
price = 10            #integer
rating = 4.9          #floating point number
name = 'Mekhrol'      #string
is_published = True   #Boolean
print(price)
#We check in a patient named John Smith He's 20 years old and is a new patient
full_name = 'John Smith'
age = 20
is_new = True

#-----------------------------------------------------------------------

#Receiving input
name = input('What is your name? ')
color = input('What is your favourite color? ')
print(name + ' likes ' + color)

#-----------------------------------------------------------------------

#Type Conversion
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2021 - int(birth_year)
print(type(age))
print(age)

weight_lbs=input('Weight (lbs): ')
weight_kg = 0.45*float(weight_lbs)
print(weight_kg)

#-----------------------------------------------------------------------

#strings
course = 'Python for Beginners'
print(course[0:3])  #not h  - pyt
print(course[1:])   #first character removed
another = course[:]
print(another)
name = 'Jennifer'
print(name[1:-1])   #ennife  excluded r

#-----------------------------------------------------------------------

#formatted strings
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)

#-----------------------------------------------------------------------

#string methods  00:40:50
course = 'Python for Beginners'
print(len(course))    
print(course.upper())      #creates new string and outputs
print(course.lower()) 
print(course)              #same original
print(course.find('P')) 
print(course.replace('Beginners', 'Absolute Beginners')) 
print('Python' in course)  #returns boolean value
print(course.title())      #uppercases the first letter of the word
