# taking two inputs from the user
a=float(input("Enter the first number (a):"))
b=float(input("Enter the second number (b):"))

#Floor division
floor_division_result = a//b
print("Floor division",floor_division_result)
#Exponentiation (a power b)
exponentiation_result = a ** b

#check if the variables are equal 
are_equal = a == b

#Printing the results 
print(f"floor Division (a//b): {floor_division_result}")
print(f"Exponentiation Division (a**b): {exponentiation_result}")
print(f"Are a and b equal?{are_equal}")
