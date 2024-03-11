# it help to perform operation between two operands . 

# Arithmetic Operator
# COmparison operator
# Logical  operator
# Membership operator
# Identity operator

# Assignment Operator
# Bitwise operator



# Arithmetic Operator
    # Addition        => a=10 b=5 => a+b = 20 
    # Subtraction     => a=10 b=5 => a-b = 15
    # Multiplication  => a=10 b=5 => a*b = 50
    # divide          => a=10 b=5 => a/b = 2.0
    # remainder       => a=10 b=5 => a%b = 0
    # Exponent        => a=10 b=5 => a**b = 50      10**5 => 10*10810*10*10
    # Floor divison   => a=10 b=5 => a//b = 50     


num1=10
num2=5

print(num1+num2)                            # addition ans : 15 
print(num1-num2)                            # substraction ans: 5
print(num1*num2)                            # multiplication ans : 50
print(num1/num2)                            # division ans : 2.0
print(num1%num2)                            # Remainder or modulus ans : 0
print( num1**num2)                          # exponential ans : 100000
print( num1//num2 )                         # floor division ans : 2


# Comparison operator 

# ==   => if two operans are equal  then True else False
# !=   => if two operans are not equal then True else False
# >    => if left side value is greater is True else False 
# <    => if left side value is smaller  is True else False 
# >=   => if left side value is greater than or equal is True else False  
# <=   => if left side value is smaller than or equal is True else False 

a=10
b=5
print(a==b)   #False
print(a!=b)   #True
print(a>b)    #True
print(a>=b)   #True
print(a<=b)   #False
print(a<b)    #False



# Logical  operator

# and => both operand must be  true for the result to be True otherwise false
# or  => either of one operand can be true for the result to be True otherwise false
# not => if my expression a is true then result will be false . 

a=10
b=5

print((a>b)and(b<a))  # True
print((a>b)or(b>a))   # True
print(not(a>b))       # False


# membership Operator : => it help to find the valus is present or not . 

# in 
# not in 

flowers=["Rose","Lily","Daffodil"]
print("Rose"in flowers )         # True
print("Marigold"not in flowers)  # True

# Identity Operator => 
# is    => checks the identity , means whether they are same or not.
# is not=> checks the non-identity, means whether they are different or not.

x = 10
y = 10
z = "10"

print(x is y)          # True
print(x is z)          # False
print(x is not z)      # True



