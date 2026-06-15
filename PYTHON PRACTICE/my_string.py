# city = 'Bhopal'
# print(city[0])
# print(city[2])
# print("---------------------------")

# print(city[-1])
# print(city[5])
# print("---------------------------")

# print(city[-3])
# print(city[3])
#------------------------------------------------

# name = 'priya sharma'
# print(name[0:5])
# print(name[6:])
# print(name[:5])
# print(name[::2])
# print(name[::-1])
# print(len(name))
#----------------------------------------------

# text = '  Hello Python World!  '
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())     #use for alternate the first character of every word in different case

# print(text.strip())     #use for removings the space area from starting and ending of the string

# print('Python in text')
# print(text.find("Python"))   # this shows the starting index of the word we want to find
# print(text.count('l'))

# print(text.replace('Python', 'Ai'))
#-------------------------------------------------------------------------------------------------

# #split and join

# csv = 'Rahul,22,Bhopal,Engineer'
# parts=csv.split(',')
# print(parts)
# print(parts[0])

# rejoined = ' | '.join(parts)
# print(rejoined)
# #-----------------------------------------------------

# #check content
# print('hello123'.isalnum())    # check if any one digit is present here or not
# print('123465'.isdigit())     # check all the number is digit or not
# print('Python'.isalpha())     # check all alphabetes or not
# print('   '.isspace())        #check all space or not
# #-------------------------------------------------------

# #start/end check

# email = 'abc2927@gmail.com'
# print(email.endswith('.com'))
# print(email.startswith('stu'))
#-----------------------------------------------------

##### F STRING #######
# name,marks,rank = 'Anita', 92.567, 3
# print(f'Hello, {name}!')

# #Format numbers
# print(f'Marks: {marks:.2f}')
# print(f'Marks: {marks:.0f}')
# print(f'count: {1000000:,}')

# # padding and allignment
# print(f'{name:<15}|{marks:>8.2f}|rank:{rank}')

# #Expression inside {}
# price, gst = 500, 0.18
# print(f'Price:rs.{price} | gst:rs.{price*gst:.2f} | total:rs.{price*(1+gst):.2f}')
#----------------------------------------------------------------

# string = "Hello, How are you doing today?"
# #count vowels in this string
# #print you from the string
# #print the string in reverce order

# print(string.find('you'))
# print(string[15:18])


# non_palin, palin = "abcdef", "axttxa"
# #check if the string is palindrome or not

# print(string[::-1])
# #-------------------------------
# if palin==palin[::-1]:
#     print("word is palindrome")
# else:
#     ("word is not palindrome")

# #--------------------------
# count = 0
# for ch in string:
#     if ch.lower() in "aeiou":
#         count += 1
# print("vowels",count)

#--------------------------------------

