# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset

# Step 1: Load the dataset
try:
    df = pd.read_csv('student marks.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'student marks.csv' not found.")
    exit()

# Step 2: Display first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Step 3: Explore data types and missing values
print("\nData types and non-null counts:")
print(df.info())

print("\nMissing values in each column:")
print(df.isnull().sum())

# Step 4: Clean missing values
df = df.dropna()  # Alternatively, you can use df.fillna()

print("\nData after dropping missing values:")
print(df.info())

# Task 2: Basic Data Analysis

# Step 1: Basic statistics
print("\nDescriptive statistics:")
print(df.describe())

# Step 2: Grouping - e.g., average marks per subject
# Assuming the dataset has a 'Class' and 'Marks' column
if 'Class' in df.columns and 'Marks' in df.columns:
    print("\nAverage marks per class:")
    print(df.groupby('Class')['Marks'].mean())
else:
    print("\nCould not perform group analysis - 'Class' or 'Marks' column missing.")

# Task 3: Data Visualization

# Set Seaborn style
sns.set(style="whitegrid")

# Line Chart - Assume there's a 'Date' column
if 'Date' in df.columns and 'Marks' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])  # Convert to datetime
    df_sorted = df.sort_values('Date')
    plt.figure(figsize=(10, 5))
    plt.plot(df_sorted['Date'], df_sorted['Marks'], marker='o')
    plt.title('Student Marks Over Time')
    plt.xlabel('Date')
    plt.ylabel('Marks')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("\nSkipping line chart - 'Date' column not found.")

# Bar Chart - Average marks per class
if 'Class' in df.columns and 'Marks' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x='Class', y='Marks', estimator='mean', ci=None)
    plt.title('Average Marks per Class')
    plt.xlabel('Class')
    plt.ylabel('Average Marks')
    plt.show()

# Histogram - Distribution of Marks
if 'Marks' in df.columns:
    plt.figure(figsize=(8, 5))
    plt.hist(df['Marks'], bins=10, edgecolor='black')
    plt.title('Distribution of Student Marks')
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    plt.show()

# Scatter Plot - e.g., 'Math' vs. 'Science' scores (if such columns exist)
if 'Math' in df.columns and 'Science' in df.columns:
    plt.figure(figsize=(8, 5))
    plt.scatter(df['Math'], df['Science'], alpha=0.7)
    plt.title('Math vs. Science Scores')
    plt.xlabel('Math')
    plt.ylabel('Science')
    plt.show()

# Optional: Save cleaned dataset
df.to_csv('cleaned_student_marks.csv', index=False)
