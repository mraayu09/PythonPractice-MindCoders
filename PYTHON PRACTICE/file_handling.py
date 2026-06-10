# with open("data.txt", "r") as file:
#     data = file.read()

# print(data)
#-------------------------------------

with open('students.txt', 'w') as f:
    f.write('Rahul Sharma,85,bhopal\n')
    f.write('priya verma,92,indore\n')
    f.write('amit kumar,73,jabalpur\n')
    

with open('students.txt', 'a') as f:
    f.write('sneha joshi,88,bhopal\n')


with open('students.txt', 'r') as f:
    content = f.read()
print(content)


with open('students.txt', 'r') as f:
    for line in f:
        name,marks,city = line.strip().split(',')
        print(f'{name:<15} | {marks:>5} | {city}')
        print("--------------------")
    