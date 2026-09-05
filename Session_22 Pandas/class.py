import pandas as pd#pip3 install pandas

sales = pd.Series([100,200,300,400,500])
print(sales)

sales = pd.Series([100,200,300,400,500], index=['jan','feb','march','apr','may'])
print(sales['march'])#300

#dataframe

df ={
    "Name":[
        "John",
        "Alice",
        "Bob",
        "Aanya",
        "Ishaan"
    ],
    "Departments": [
        "IT",
        "HR",
        "Finance",
        "IT",
        "HR"
    ],
    "Age":[
        25,
        30,
        28,
        24,
        29
    ],
    "Sales": [
        1200,
        1500,
        1100,
        1300,
        1400
    ]
}

df = pd.DataFrame(df)
print(df)

print(df.head(3))#first 3 rows
print(df.tail(2))#last 2 rows
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())

print(df['Name'])#single column
print(df['Name','Salary'])#multiple column

print("First Row : ",df.iloc[0])#first row
print("First Row : ",df.iloc[0:3])#first three rows
print("First Row : ",df.iloc[0,0:3])#first  row and thre e co.umns
print("First Row : ",df.iloc[0:3,0:2])#first three rows and 2 columns

highest_sale = df[(df['Sales']>1300) & (df['Departments']=='HR')]
print(highest_sale)

df['Location'] = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(df)
df['Corrected Age'] = df['Age'] - 2

sales_sort = df.sort_values("Sales", ascending=False) 

print(df['Sales'].mean())
print(df['Sales'].max())
print(df['Sales'].min())
print(df['Sales'].sum())

print(df.value_counts('Departments'))#count of each department

department_sales = df.groupby('Departments')['Sales'].sum()
print(department_sales)

departmetn_details = df.groupby('Departments').agg(
    Average_Sale =("Sales","mean"),
    Total_Sale =("Sales","sum"),
    Employee_Count =("Name","count"),
)

print(df.isnull())
print(df.isnull().sum())

df['Departments'] = df['Departments'].fillna('Review')
df['Sales'] = df['Sales'].fillna(0)

df_without_age = df.drop(columns=["Age"])
print(df_without_age)