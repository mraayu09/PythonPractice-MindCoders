# print("hello")

#----------------------------------------#

# There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5 Your task is to:
# write a line of code that prints the length of the existing list (Step 1).
# write a line of code that removes the last element from the list (Step 2)
# write a line of code that prompts the user to replace the middle number in the list
#  with an integer number entered by the user (Step 3)

# hat=[1,2,3,4,5]
# length=len(hat)
# print(length)
# # del hat[-1]
# # print(hat)
# middle=length//2
# print(middle)
# hat[middle]=input("enter the number")
# print(hat)
#--------------------------------------------------------------------------------------------------------------#

# The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history.
#  Some people consider them to be the most influential act of the rock era.
#  Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.
# The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).
# Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:
# step 1: create an empty list named beatles;
# step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# step 5: use the insert() method to add Ringo Starr to the beginning of the list.

# beatles=[]
# beatles.append("john lennon")
# beatles.append("paul mccartney")
# beatles.append("george harrison")
# print(beatles)
# for i in range(2):
#     new=input("give member name: ")
#     beatles.append(new)
# print(beatles)    

# del beatles[3]
# del beatles[3]
# print(beatles)

# beatles.insert(0,"ringo starr")
# print(beatles)

#------------------------------------------------------------------------------------------------------------------------------------------------#

# Practice Question: Loops
# Write a program to print numbers from 1 to 50 in this pattern
# [1, 2, Fiz, 4, Buzz, Fiz, 7, 8, Fiz, Buzz, 11, Fiz, 13, 14, FizBuzz, 16....50]
# Write a Program to Count Numbers of Digits in this String
# Input: string = "MindCoders password2 is : 1234"
# Output: Total number of Digits = 5
# Write a Program to Count Numbers of Digits in this String
# Input: string = "U r a a n S 0 f t s k i l l 1 s 1234"
# Output: Total number of Digits = 6
# Write a program to find the count for the occurrence of 's' or 'S' character in a string
# Input: "MindCoders"
# Output: 3

# # 1-----
# for i in range(1,51):
#     if i%3==0 and i%5 ==0:
#         print("FizBuzz", end=", ")

#     elif i%3==0:
#         print("Fiz",end=", ")

#     elif i%5 == 0:
#         print("Buzz",end=", ")

#     else:
#         print(i, end=", ")         

# # 2-------
# string="mindcoders password 2 is: 1234"   
# count=0
# for i in string:
#     if i.isdigit():
#         count += 1
# print("total digit in the string is:",count)    

#---------------

# # 3---------
# string="U r a a n S 0 f t s k i l l 1 s 1234"
# count=0
# for i in string:
#     if i.isdigit():
#         count += 1
# print("total digits", count)        
#---------------------------------

# # 4---------
# string="MindCoders"
# count=0
# for i in string:
#     if i =='s' or i=='S':
#         count += 1
# print ("total count",count)        
#--------------------------------------------------
###-----------------------=====================-------------------------------========================-----------------------------------------------###

# Practice Question: Loops
# Write a program to count the number of repeated characters and unique characters in a string
# Input: "UraanSoftskills"
# Write a program to find the frequency of each character in a given string
# Input: "UraanSoftskills"
# You must design the (ugly) vowel eater! Write a program that uses:
# a for loop;
# the concept of conditional execution (if-elif-else)
# the continue statement.
# Your program must:
# ask the user to enter a word;
# use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about string methods and the upper() method very soon - don't worry;
# use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
# assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.

# # 1---------------------
# string="UraanSoftskills"
# lower=string.lower()
# repeat_count=0
# unique_count=0
# for i in set(lower):
#     if lower.count(i)>1:
#         repeat_count += 1
#     else:
#         unique_count += 1

# print("repeat:",repeat_count)
# print("unique",unique_count)            
#=------------------------

# # 2--------------------
# string="UraanSoftskills"
# frequency ={}
# for i in string:
#     if i in frequency:
#         frequency[i] += 1
#     else:
#         frequency[i] =1
# print("character frequency:", frequency)            
#---------------------------

# # 3---------------
# string = input("enter a word: ")
# string=string.upper()
# vowel_less = ""

# for letter in string:
#     if letter =="A":
#         continue
    
#     elif letter =="E":
#         continue
#     elif letter =="I":
#         continue
#     elif letter =="O":
#         continue
#     elif letter =="U":
#         continue
#     else:
#         vowel_less += letter
# print("word without vowels is :",vowel_less)        
###=========================================================================================================###

# Practice Question: Loops
# 1. Write a program to print the first 10 natural numbers using for loop
# 2. Write a program to print all the even numbers within the range of 10
# 3. Write a program to calculate the sum of all numbers from 1 to a given number - 15
# 4. Write a program to calculate the sum of all the odd numbers within the given range of 15
# 5. ⁠Write a program to print a multiplication table of a given number 15
# 6. ⁠Write a program to display numbers from a list using a for the loop [1,2,4,6,88,125]
# 7. ⁠Write a program to count the total number of digits in a number 129475
# 8. ⁠Write a program to check if the given string is a palindrome - madam
# 9. ⁠Write a program that accepts a word from the user and reverses it
# 10. ⁠Write a program to check if a given number is an Armstrong number 153

# 1--------------
for i in range(1,11):
    print(i, end=" ")

# 2 ----------------
for i in range(2,11,2):
    print(i,end="")    

# 3----------------
sum=0
for i in range(1,16):
    sum += i
print("sum is:",sum)

# 4----------------
odd_sum=0
for i in range(1,16):
    if i%2 != 0:
        odd_sum += i
print("sum of all odd numbers is:",odd_sum)        

# 5------------------
n=15
for i in range(1,11):
    print(n,"x",i,"=",n*i)


# 6 -----------------
list=[1,2,4,6,88,125]
for i in list:
    print(i, end=" ")

# 7 -----------------
number=127495
count=len(str(number))
print("total digit of the number is:",count)

# 8 -----------------
word="madam"
if word == word[::-1]:
    print("word is palindrome")

else:
    print("word is not a palindrome")

# 9 -----------------
word= input("enter word")
reverse_word=word[::-1] 
print("reverse word is",reverse_word)       

# 10 ----------------
n=153
c=n
ar