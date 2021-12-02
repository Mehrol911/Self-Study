#weight program converter
Weight = int(input("Weight: "))
unit = input("(L) bs or (K)g: ")
if unit.upper() =="L": 
   converted = Weight * 0.45
   print(f"You are {converted} kilos")
elif unit.upper() =="K":
    converted = Weight // 0.45
    print(f"You are {converted} pounds")
else: 
    print("Write proper value")   
