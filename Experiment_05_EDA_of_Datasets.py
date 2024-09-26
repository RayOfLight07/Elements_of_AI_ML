# Using Python language do the exploratory data analysis of dataset imported in the lab 4.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset (update the file path)
df = pd.read_csv('C:/Users/nitro/OneDrive/Desktop/Programming/Elements of Ai Ml EXP/Exp_04_dataset.csv')
# 1. Overview of the dataset
print("\nDataset Overview:")
print(df.info())

# 2. Statistical summary of numerical columns
print("\nStatistical Summary of Numerical Columns:")
print(df.describe())

# 3. Visualizing missing data
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Data Heatmap')
plt.show()

# 4. Distribution of numerical columns
df.hist(figsize=(12, 8), bins=20)
plt.suptitle('Histogram of Numerical Columns')
plt.show()

# 5. Correlation between numerical columns (filtering out non-numerical columns)
plt.figure(figsize=(10, 6))

# Select only numerical columns for correlation
numerical_df = df.select_dtypes(include=['float64', 'int64'])

# Plot correlation heatmap
sns.heatmap(numerical_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Numerical Columns')
plt.show()

# 6. Pairplot for numerical columns
sns.pairplot(numerical_df)
plt.suptitle('Pairplot of Numerical Columns', y=1.02)
plt.show()

# 7. Boxplot to check outliers in numerical columns
plt.figure(figsize=(12, 6))
sns.boxplot(data=numerical_df)
plt.title('Boxplot for Numerical Columns')
plt.xticks(rotation=90)
plt.show()

# 8. Value counts for categorical columns (if any)
for column in df.select_dtypes(include=['object']).columns:
    print(f"\nValue counts for {column}:")
    print(df[column].value_counts())
