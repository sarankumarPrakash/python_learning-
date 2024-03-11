# Standard data types :

# 1. Numbers
# 2. dictionary
# 3. boolean
# 4. set 
# 5. tuple
# 6. list 
# 7. string 

# Numbers : 

num = 10   # integer
print(type(num))

num_complex = 1 +  1j  # complex number
print(type(num_complex))

num_float = 10.5  # Float
print(type(num_float))


# string :

strng = "Hello, World!"
print(type(strng))

# Boolean:

booln = True or False
print(type(booln))


# List   => thses are like array but can able to store of different data type []

list=[1,"hi","python",2,True]
print(type(list))  

# tuple => these are same like List but paranthesis  used instead of square bracket and they are immutable   ().

tup= (1,"Hi","Python",2,True)
print(type(tup))

# set => These are same like list but same using curly barsis  {} and they only stores unique element .
set_lst = [1,2,2,3,4,4,5]
print("List : ",set_lst)

set_val = set(set_lst)
print("Set Value : ",set_val)

#Dictionary  => these are like objects used to store value in key:value pairs  {}

dic={1:'jimmy',2:'arun',3:'David'}
print(type(dic))
