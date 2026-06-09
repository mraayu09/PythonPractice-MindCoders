# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("Division failed")
#         return None
#     else:
#         print("Everything went fine")
#         return n
# print(reciprocal(2)) # Uses else branch
# print(reciprocal(0))

#=====================================================

# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("Division failed")
#         n = None
#     else:
#         print("Everything went fine")
#     finally:
#         print("It's time to say goodbye")
#     return n
    
# print(reciprocal(2))
# print("------------------------------")
# print(reciprocal(0))
#-----------------------------------------

# try:
#     i = int("Hello!")
# except Exception as e:
#     print(e)
#     print(e.__str__())
#--------------------------------------------

#How to create your own exception

class MyZeroDivisionError(ZeroDivisionError):
    pass
def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:
        raise ZeroDivisionError("some bad news")
    
do_the_division(False)