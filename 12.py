import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Department': ['HR', 'IT', 'Finance', 'IT', 'Finance', 'HR', 'HR', 'Finance', 'IT', 'Finance'],
    'Salary': [20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000]
}
df = pd.DataFrame(data)

# Set style
sns.set(style='whitegrid')

# Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Department', y='Salary', hue='Department',palette="Set2")  # Palette name corrected

plt.title("Box & Whiskers Plot of Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()
