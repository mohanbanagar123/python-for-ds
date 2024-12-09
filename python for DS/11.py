import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data={
    'Age':[25,30,35,40,45,50,55,60,65,70],
    'Salary':[20000,25000,30000,35000,40000,45000,50000,55000,60000,65000],
    'Department':['HR','IT','Finance','IT','Finance','HR','HR','Finance','IT','Finance']
}
df=pd.DataFrame(data)

plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='Age', y='Salary', hue='Department', palette='viridis',s=100)
plt.title("Scatter plot of Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend(title='Department')
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(data=df, x='Age', bins=5, kde=True,color='purple')
plt.title("Histogram of Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Department')
plt.title("Bar plot of Department counts")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.show()
