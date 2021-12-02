#Functions and Keyword arguments 20/11/2021
def greet_user(first_name, last_name):
    #name = "John"
    print(f'Hi {first_name} {last_name}!') #formatted string
    print('Welcome aboard')

#actual piece of information = argument
print("Start")
greet_user("John", "Smith") #type error if we miss one of them,  #positional argument
greet_user(last_name="Mary", first_name="Shelly") #keywoard argument
print("Finish")

#-----------------------------------------------------------------------
#return statement #02:44:45
def square(number):
    return number*number


#result = square(3)
print(square(3))

#Creating a Reusable Function
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
         ":)": "😄",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(emoji_converter(message))
#-----------------------------------------------------------------------
#Exceptions
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
    print('Invalid value')

#-----------------------------------------------------------------------
#Comments
print("Sky is blue")

#-----------------------------------------------------------------------
#Classes 03:01:46
class Point: #Pascal naming convention MekhrolBazarov
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()
