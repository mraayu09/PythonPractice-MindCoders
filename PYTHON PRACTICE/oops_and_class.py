# class ExampleClass:
#     def __init__(self, val = 1):
#         self.first = val

#     def set_second(self, val):
#         self.second = val

# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
# example_object_2.set_second(3)
# example_object_3 = ExampleClass(4)
# example_object_3.third = 5

# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)

#-----------------------------------------------------------

# class Classy:
#     def method(self):
#         print("method")

# obj = Classy()
# obj.method()

#0-------------------------------------------------

# class Classy:
#     def method(self,par):
#         print("method",par)
# obj = Classy()
# obj.method(1)
#--------------------------------------------

# class Classy:
#     varia = 2
#     def method(self):
#         print(self.varia, self.var)

# obj = Classy()
# obj.var = 3
# obj.method()
#--------------------------------------------

# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy

# sun = Star("Sun", "Milky Way")
# print(sun)
#------------------------------------------------

# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy

#     def __str__(self):
#         return self.name + ' in ' + self.galaxy
    
# sun = Star("Sun", "Milky Way")
# print(sun)

#------------------------------------------------

# class Vehicle:
#     pass
# class LandVehicle(Vehicle):
#     pass
# class TrackedVehicle(LandVehicle):
#     pass                                # this is an example of inheritense this is not working but for understanding

#----------------------------------------------------

# class Vehicle:
#     pass
# class LandVehicle(Vehicle):
#     pass
# class TrackedVehicle(LandVehicle):
#     pass

# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(issubclass(cls1, cls2), end="\t")    #\t for tab ke liye use hua h
#     print()
#-----------------------------------------------------

# class Super:
#     supVar = 1
# class Sub(Super):
#     subVar = 2

# obj = Sub()
# print(obj.subVar) 
# print(obj.supVar)    # example od inheritance
#-------------------------------------------------------------
# class Super:
#     def __init__(self):
#         self.supVar = 11

# class Sub(Super):
#     def __init__(self):
#         super().__init__()   # child class me parnt class ka constructer call karna jaruri hota h otherwise error
#         self.subVar = 12

# obj = Sub()
# print(obj.subVar) 
# print(obj.supVar)
#------------------------------------------------------------

# class Level1:
#     variable_1 = 100
#     def __init__(self):
#         self.var_1 = 101
#     def fun_1(self):
#         return 102
    
# class Level2(Level1):
#     variable_2 = 200
#     def __init__(self):
#         super().__init__()
#         self.var_2 = 201
#     def fun_2(self):
#         return 202
    
# class Level3(Level2):
#     variable_3 = 300
#     def __init__(self):
#         super().__init__()
#         self.var_3 = 301
#     def fun_3(self):
#         return 302
    
# obj = Level3()
# print(obj.variable_1, obj.var_1, obj.fun_1()) 
# print(obj.variable_2, obj.var_2, obj.fun_2()) 
# print(obj.variable_3, obj.var_3, obj.fun_3())  
#-----------------------------------------------------------

# v=input("enter your word : ")
# print("I Am",v,"better than you.")
# print(4*(f"{v} ")+v)
#------------------------------------------------------

# class Super:
#     def __init__(self,name):
#         self.name= name

#     def __str__(self):
#         return "My name is "+ self.name + "."
    
# class Sub(Super):
#     def __init__(self,name):
#         Super.__init__(self,name)

# obj = Sub("Andy")
# print(obj)
#----------------------------------------------------


# class Super:
#     def __init__(self,name):
#         self.name= name

#     def __str__(self):
#         return "My name is "+ self.name + "."
    
# class Sub(Super):
#     def __init__(self,name):
#         super().__init__(name)

# obj = Sub("Andy")
# print(obj)
#--------------------------------------------

# MUltiple inheritence example
# class SuperA:
#     var_a = 10
#     def fun_a(self):
#         return 11
    
# class SuperB:
#     var_b = 20
#     def fun_b(self):
#         return 21
    
# class Sub(SuperA, SuperB):
#     pass

# obj = Sub()
# print(obj.var_a, obj.fun_a()) 
# print(obj.var_b, obj.fun_b())
#-------------------------------------------------------

# # # multilevel inheritence
# # class Level1:tiple Inheritance Conflicts
# class Left:
#     var = "L"
#     var_left = "LL"
#     def fun(self):
#         return "Left"
# class Right:
#     var = "R" # Same name as Left.var
#     var_right = "RR"
#     def fun(self): # Same name as Left.fun()
#         return "Right"
# class Sub(Left, Right):
#     pass
# obj = Sub()
# print(obj.var, obj.var_left, obj.var_right, obj.fun())
#---------------------------------------------------------------------
#     var = 100
#     def fun(self):
#         return 101
    
# class Level2(Level1):
#     var = 200                 # Overrides Level1.var
#     def fun(self):            # Overrides Level1.fun()
#         return 201
    
# class Level3(Level2):
#     pass

# obj = Level3()
# print(obj.var, obj.fun())
# # bottom to top apprach par kaam karta h jo bhi functiom last me call hoga whi print ho jayga
#====------------------------------------------------------------------------

#Mul
#--------------------------------------------------------

# class One:
#     def do_it(self):
#         print("do_it from One")

#     def doanything(self):
#         self.do_it()

# class Two(One):
#     def do_it(self):
#         print("do_it from Two")

# one = One()
# two = Two()
# one.doanything() 
# two.doanything()
#-------------------------------------------------------------

