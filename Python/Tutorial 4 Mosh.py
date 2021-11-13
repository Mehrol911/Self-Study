#while loops 01:20:43    
i = 5
while i >= 1:
    print('*' * i)
    i = i - 1
print("Done")    

#for loops  01:41:48
for item in 'Python': #[numbers, names]
    print(item)
for item in range(5, 10, 2): # 2 steps after 5
    print(item)
#exercise
prices=[10,20,30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

#nested loops
for x in range(4):
    for y in range(3):  #inner loop
        print(f'({x},{y})')
#exercise
numbers = [2,2,2,2,5] #F 5,2,5,2,2
for x_count in numbers:
    #print('x' * x_count) 
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

#lists 
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0]='Jon'
print(names[:]) #new list []

numbers = [5,6,8,9,12,54]
print(max(numbers))

#using for and if
numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#2D lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

#list methods
numbers = [5, 2, 1, 5, 7, 4]
numbers.append(20)
numbers.insert(0, 10)
numbers.remove(5) # clear deletes all elements
numbers.pop() #deletes the last element it means the top element (stack)
print(numbers)
print(numbers.index(2)) # finding index of the number
print(50 in numbers) #checking is there 50 or not (we will get boolean value)
print(numbers.count(5)) #count 5
numbers.sort()
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)

#exercise
numbers = [4, 5, 6, 7, 5, 4, 6, 7, 4, 3, 2]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
