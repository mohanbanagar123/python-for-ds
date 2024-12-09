import pandas as pd

# Create DataFrame
data = {
    'Name': ['Alice', 'BOB', 'CHARLIE', None, 'Eve'],
    'Age': [25, None, 30, None, None],
    'City': ['New York', 'Los Angeles', None, 'Chicago', 'Miami'],
}
df = pd.DataFrame(data)

# Analyze missing data
print("DataFrame:\n", df)
print("\nMissing Data Analysis:")
print("Missing values in each column:\n", df.isnull().sum())
print("\nPercentage of missing values:\n", (df.isnull().mean() * 100))

# Handle missing data
choice = input("\nChoose: 1.Fill, 2.Drop Rows, 3.Drop Columns: ")
if choice == '1':
    value = input("Value to fill missing data: ")
    df = df.fillna(value)
elif choice == '2':
    df = df.dropna()
elif choice == '3':
    df = df.dropna(axis=1)
else:
    print("Invalid choice!")

print("\nUpdated DataFrame:\n", df)
