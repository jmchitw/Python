name = input("What is your name? \n")
age = int(input("What is your age? \n"))
decades = age // 10
years = age % 10
print("\n" 
      + name + 
      ", you are " + 
      str(decades) + 
      " decades and " +
      str(years) + 
      " years old!\n")

# The above code can be simplified using f-strings as shown below:
print(f"{name}, you are {decades} decades and {years} years old!\n")


