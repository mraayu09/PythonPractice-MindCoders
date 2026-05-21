# row=[]
# for i in range(8):
#     row.append("WHITE_PAWN")

# print(row)    

#another way
# row=["WHITE_PAWN" for i in range(8)]
# print(row)

# squares=[x**2 for x in range(10)]
# print(squares)

# squares=[x**2 for x in range(1,11)]
# print(squares)

# twos=[2**i for i in range(8)]
# print(twos)

# squares=[x**2 for x in range(1,11)]
# odds=[x for x in squares if x%2 != 0]
# print(odds)

# list=[]
# for i in range(8):
#     row=["A" for i in range(8)]
#     list.append(row)

# for i in list:
#     print(i)

# print(len(list))        
# print(list[0][0])  # first index is row no. and second is column no.

# list=[]
# for i in range(8):
#     row=["A" for i in range(8)]
#     list.append(row)

# list[0][0] = "Rooks"
# list[0][7] = "Rooks"
# list[7][0] = "Rooks"
# list[7][7] = "Rooks"

# for element in list:
#     print(element)

# list=[]
# for i in range(8):
#      row=["A" for i in range(8)]
#      list.append(row)

# list[0][0] = "Rook"
# list[0][7] = "Rook"
# list[7][0] = "Rook"
# list[7][7] = "Rook"

# list[0][1] = "Night"
# list[0][6] = "Night"
# list[7][1] = "Night"
# list[7][6] = "Night"

# for element in list:
#     print(element)

## comprihension under comprihension
# temps=[[0.0 for h in range(24)] for d in range(31)]   # 24 rows and 31 column
# for element in temps:
#     print(element)



# temps=[[0.0 for h in range(24)] for d in range(31)]
# temp1=19
# temp2=32
# count=0

# for days in temps:
#     if count==0:
#         days[11]=temp1
#         count=1
#     else:
#         days[11]=temp2
#         count=0   

# for element in temps:
#     print(element)

# total=0.0
# for days in temps:
#     total += days[11]

# average = total/31
# print("average temprature at noon:",average)        

# highest = -100.0
# for day in temps:
#     for temp in day:
#         if temp>highest:
#             highest=temp
# print("The highest temrature was:", highest)            

# hot_days=0
# for day in temps:
#     if day[11]>20.0:
#         hot_days += 1
# print("hot days in the month :",hot_days)        