try:
    name = input("enter your name").strip()
    age = int(input("enter your age"))
    if age < 0:
         print("Input cannot be negative")

    elif age > 100:
         print("you are lying")

    elif age < 18:
         print("Minor")
         
    else:
         print("adult")
       

    print("valide age",age)
    print("name",name)  
except ValueError:
    print("Invalid age. Must be a number")