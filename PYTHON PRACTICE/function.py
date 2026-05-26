# def message():
#     print("enter the value: ")

# message()  
# a=int(input())

# message()
# b=int(input()) 

# message()  
# c=int(input())
#-------------------------------

# def massage():
#     print("enter a value")

# print("we start here.")
# print(massage)
# massage()
# print("we end here.")    
#-------------------------------

# def message():
#     print("enter a value: ")
#     temp=int(input())
#     return temp

# print("step 1")
# a = message()

# print("step 2")
# b = message()

# print("step 3")
# c = message()

# print("a:",a)
# print("b:",b)
# print("c:",c)
#----------------------------

# def hello(n):
#     print("Hello,",n)

# name=input("enter your name:")
# hello(name)    
#=-------------------------------

# def message(number):
#     print("enter a number:",number)

# number=1234
# message(1)
# print(number)    
#-------------------------------

# def message(what,number):
#     print("enter",what,"number",number)

# message("telephone",11)
# message(11,"telephone")
# message("price",5)
# message("number","number")
#--------------------------------    

# def introduction(first_name,last_name):
#     print("Hello,my name is",first_name,last_name)

# introduction("luke","skywalker")
# introduction("jese","quick")
# introduction("clark","kent") 

# introduction(first_name="james", last_name="bond")
# introduction(last_name="skywalker",first_name="luke")
# #-----------------------------------------------------

# def adding(a, b, c):
#     print(a, "+", b, "+", c, "=", a + b + c)
# adding(1, 2, 3)
# adding(c = 1, a = 2, b = 3)
# adding(3, c = 1, b = 2)
# adding(3, a = 1, b = 2)
#---------------------------------------------------------

# def happy_new_year(wishes = True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return
#     print("Happy New Year!")
# happy_new_year()
# # happy_new_year(False)
#------------------------------------------------------------

# def boring_function():
#     print("'Boredom Mode' ON.")
#     return 123
# print("This lesson is interesting!")
# boring_function()
# print("This lesson is boring...") 
#----------------------------------------------------------------

# def checkMyVar(variable):
#     if(variable == 10):
#         print("variable is 10")
#         return 2
#     else:
#         print("variable is not up to the mark")
#         return
# checkMyVar(10)   
# # checkMyVar(5)
# print()    
#---------------------------------------------------------------

# def list_sum(lst):
#     s=0

#     for elem in lst:
#         s += elem

#     return s
# print(list_sum([5,4,3]))    
# print(list_sum(2))
#---------------------------------------------------------------

# def strange_list_fun(n):
#     strange_list = []

#     for i in range(0, n):
#         #strange_list,insert(0,i+1)
#         strange_list.append(i+1)
#     return strange_list
# print(strange_list_fun(5))
#----------------------------------------------------------------------

### FUNCTION AND SCOPE


# def scope_test():
#     x = 123
# scope_test()
# print(x)
#-----------------------------------------------

# def my_function():
#     print("Do I know that variable?", var)
# var = 1
# my_function()
# print(var)
#-----------------------------------------------

# def mult(x):
#     var = 7
#     return x * var
# var = 3
# print(mult(7))
#-----------------------------------------------

# def my_function():
#     global var
#     var = 2
#     print("Do I know that variable?", var)
# var = 1
# my_function()
# print(var)
#-----------------------------------------------

# var = 2
# print(var)

# def return_var():
#     global var
#     var = 5
#     return var

# print(return_var())
# print(var)
#-------------------------

# def my_function(n):
#     print("I got", n)
#     n += 1
#     print("I have", n)
# var = 1
# my_function(var)
# print(var)
#-------------------------

# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     my_list_1 = [0, 1]
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)
#------------------------------------

# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     del my_list_1[0] # Pay attention to this line.
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)
#-----------------------------------------

### FUNCTION AND RECURSION###

# def rev(x):
#     print(x)
#     if x==0:
#         return
#     else:
#         rev(x-1)
# print("starting recursion")
# rev(5)    
# print("end recursion")
#------------------------------------
#same code and detailing in recursion
# def rev(x):
#     print(x)
#     if x==0:
#         return
#     else:
#         print("going in recursion",x)
#         rev(x-1)
#         print("out of recursion",x)
# print("starting recursion")
# rev(5)    
# print("end recursion")
#----------------------------------

# def fact(x):
    
#     if x <= 0:
#         return 1
#     else:
#         return x * fact(x-1)
# print(fact(5))
#------------------------------------------
