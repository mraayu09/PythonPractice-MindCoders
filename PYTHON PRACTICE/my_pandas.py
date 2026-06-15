import pandas as pd
# print(pd.__version__)
data = {
    'Name':['Rahul','Priya','Amit','Sneha','Vikram'],
    'Age': [22,21,23,20,24],
    'Marks': [85,92,78,83,73],
    'City':['Bhopal','Indore','Bhopal','Jabalpur','Indore'],
}
df = pd.DataFrame(data)
# print(df)
# print("=====================================")

# print(df.shape)
# print(df.head(3))
# print(df.dtypes)
# print(df.describe())
# print("=====================================")

#select columns
# print("df['Name']: \n", df['Name'])
# print(df[['Name', 'Marks']])
# print("=====================================")

# ## Filter rows
# print(df[df['Marks'] >= 85])
# print(df[df['City']=='Bhopal'])
# print( df[ (df['Marks']>=80) & (df['City'] =='Indore')])
# print("==================================")

#function ........................
# def get_grade(x):
#     if x >= 90:
#         return 'A'
    
#     elif x >= 75:
#         return 'B'
    
#     else:
#         return 'C'
    
# df['Grade'] = df['Marks'].apply(get_grade)
# print(df['Grade'])
# print("-----------------------")
# print(df)
# print("===================================================")

# groupby - like pivot table
# city_avg = df.groupby('City')['Marks'].mean()
# print(city_avg)
# print("===================================================")

######## READ REAL CSV FILE #########

# df2 = pd.read_csv('students.csv')
# df2.to_csv('clean_outpiut.csv', index=False)   # save file in different file

df2 = pd.read_csv('students.csv')
print(df2)

df2['Name']=df2['Name'].str.strip()
print(df2)


df2['Marks']=df2['Marks'].str.replace('#',"").astype(int)
print(df2)

df2['City']=df2['City'].str.replace('City',"").str.replace('Dist','')
print(df2)

df2['Grade']=df2['Grade'].str.replace(r'[*@]','',regex=True).str.strip()
print(df2)

df2.to_csv('clean_outpiut.csv', index=False)   # save file in different cleaned file




