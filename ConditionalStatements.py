# In programming conditioanl Statement is more important for that desicon allows our program to run which code 
# and shows the result.

 # if Statement 
 # if else Statement 
 # Nested if Statment 
 
 
# If Statement => this COndition checks only  one condition at a time. If it is true then it will execute the code written under that if
  
# take user input for number of students in class
num_students = int(input("Enter the total number of students: "))

# check if the number is even or odd using if statement
if num_students % 2 == 0:
    print("The number is Even.")
    
    
# if else Statement  

# this will run if the above condition fails i.e., if the number is not even.

# take user input for number of students in class
num_student = int(input("Enter the total number of students: "))

# check if the number is even or odd using if statement, 
if num_student % 2 == 0:
    print("The number is Even.")
else:
    print("The given number is Odd ")
    
# Nested if Statements :
# if I want to check multiple condition im go with elif statement ie Nested if statements 

marks=int(input("Enter your marks :"))

if marks>=95:
    print("You are in A grade ")
elif marks>=85:
    print("You are in B grade ")
elif marks>=75:
   print("You are in C grade ")
elif marks>=65: 
    print("You are in D grade ")
else:
    print("You are in F grade ")