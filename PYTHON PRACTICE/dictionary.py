# dictionary = {
#                 "cat": "chat",
#                 "dog": "chien",
#                 "horse": "cheval"
#                 }
# phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
# empty_dictionary = {}

# print(dictionary)
# print(type(dictionary))
# print(phone_numbers)
# print(type(phone_numbers))
# print(empty_dictionary)
# print(type(empty_dictionary))
# print(dictionary['cat'])
# print(phone_numbers['Suzy'])
# #-------------------------------------------------------------

# dictionary = {"cat": "chat",
#                "dog": "chien",
#                  "horse": "cheval"
#                  }
# words = ['cat', 'lion', 'horse']

# for key in words:
#     if key in dictionary:
#         print(key, "->", dictionary[key])
#     else:
#         print(key, "is not in dictionary")

# print(dictionary.keys())
# for key in dictionary.keys():
#     print(key, "-->", dictionary[key])

# print("----------------------------------")

# for key,value in dictionary.items():
#     print(key, "-->", value)

# print("----------------------------------")

# print(dictionary.items())

# print("----------------------------------")

# print(dictionary.values())

# #------------------------------------------------------------------------------------

# pol_eng_dictionary = {
#                         "zamek": "castle",
#                         "woda": "water",
#                         "gleba": "soil"
#                     }
# print("pol_eng_dictionary:", pol_eng_dictionary)

# copy_dictionary = pol_eng_dictionary.copy()

# print("copy_ictionary:",copy_dictionary)

# print("---------------------------------------------------")

# pol_eng_dictionary["zamek"] = "lock"
# item = pol_eng_dictionary["zamek"]
# print(item)

#--------------------------------------------------------------------------------------

# phonebook = {} 
# print(phonebook)

# phonebook["Adam"] = 3456783958 # create/add a key-value pair
# print(phonebook)

# del phonebook["Adam"]
# print(phonebook)
#-------------------------------------------------------------------------------------

# pol_eng_dictionary = {"kwiat": "flower"}

# pol_eng_dictionary.update(
#          {
#              "gleba": "soil"
#         })
# print(pol_eng_dictionary) 

# pol_eng_dictionary.popitem()

# print(pol_eng_dictionary)
#-------------------------------------------------------------------------------------

# pol_eng_dictionary = {
#                         "zamek": "castle",
#                         "woda": "water",
#                         "gleba": "soil"
#                     }
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary)) 

# del pol_eng_dictionary["zamek"] 
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary)) 

# pol_eng_dictionary.clear() 
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# # del pol_eng_dictionary 
# # print(pol_eng_dictionary)

#------------------------------------------------------------

student_details={}

while True:

    name=input("enter student name:")
    if name == "":
        break
    
    score=int(input(f"enter {name}'s score:"))

    if score not in range(1,11):
        break

    if name in student_details:
        student_details[name] += (score,)

    else:
        student_details[name] = (score,)    

print(student_details)

for name,mark in student_details.items():
    sum = 0
    for m in mark:
        sum += m

    print(name, "-->", sum/len(mark))    

