# import csv

# records = [
#     ['Name','Marks','City','Grade'],
#     ['Rahul',85,'Bhopal','B'],
#     ['Priya',92,'Indore','A'],
#     ['Amit',73,'Jabalpur','B'],
# ]
# with open('students.csv','w',newline='') as f:
#     csv.writer(f).writerows(records)

# with open('students.csv','r') as f:
#     for row in csv.DictReader(f):
#         print(f'{row["Name"]}: {row["Marks"]} marks  ({row["City"]})')



#-------------------------------------

# with open('students.txt', 'w') as f:
#     f.write('Rahul Sharma,85,bhopal\n')
#     f.write('priya verma,92,indore\n')
#     f.write('amit kumar,73,jabalpur\n')
    

# with open('students.txt', 'a') as f:
#     f.write('sneha joshi,88,bhopal\n')


# with open('students.txt', 'r') as f:
#     content = f.read()
# print(content)


# with open('students.txt', 'r') as f:
#     for line in f:
#         name,marks,city = line.strip().split(',')
#         print(f'{name:<15} | {marks:>5} | {city}')
#         print("--------------------")
#-----------------------------------------

# import csv

# records = [
#     ['Name','Marks','City','Grade'],
#     ['Rahul',85,'Bhopal','B'],
#     ['Priya',92,'Indore','A'],
#     ['Amit',73,'Jabalpur','B'],
# ]
# with open('students.csv','w',newline='') as f:
#     csv.writer(f).writerows(records)

# name = input("Enter student Name for search:")

# found = False

# with open('students.csv','r') as f:
#     for row in csv.DictReader(f):
#          if row["Name"] == name:
#             print(f'Found {name}')
#             print(f'{row["Name"]}: {row["Marks"]} marks  ({row["City"]})')
#             found = True
#             break
# if not found:
#     print("Student not found!!")
#-------------------------------------------

# import csv

# records = [
#     ['Name','Age','sub1','sub2','sub3'],
#     ['Aayush',25,85,90,89],
#     ['Roshni',23,75,92,79],
#     ['Vishal',26,69,87,95],
#     ['Aman',25,75,98,59],
# ]

# with open('student1.csv','w',newline='') as f:
#     csv.writer(f).writerows(records)

# name = input("Enter student Name for search:")

# found = False

# with open('student1.csv','r') as f:
#     for row in csv.DictReader(f):
#         if row["Name"] == name:
#             print(f'Found {name}')
#             print(f'{row["Name"]}: {row["Age"]} Age ,subject1=({row["sub1"]}), subject2=({row["sub2"]}), subject3=({row["sub3"]})')
#             found = True
#             break

# if not found:
#     print("Student not found!!")

