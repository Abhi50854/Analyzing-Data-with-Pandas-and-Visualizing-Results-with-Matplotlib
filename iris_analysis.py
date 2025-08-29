import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# -------------------------
# Task 1: Load and Explore
# -------------------------

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Display first few rows
print("First 5 rows of dataset:")
print(df.head())

# Check dataset info
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Drop missing values if any
df = df.dropna()

# -------------------------
# Task 2: Basic Data Analysis
# -------------------------

print("\nBasic Statistics:")
print(df.describe())

print("\nMean values grouped by species:")
print(df.groupby("species").mean())

# -------------------------
# Task 3: Data Visualization
# -------------------------

sns.set(style="whitegrid")

# 1. Line Chart (cumulative sepal length per species)
plt.figure(figsize=(8,5))
df.groupby("species")["sepal length (cm)"].cumsum().reset_index().groupby(df['species']).plot(
    x="index", y="sepal length (cm)", ax=plt.gca())
plt.title("Line Chart - Cumulative Sepal Length by Species")
plt.xlabel("Index")
plt.ylabel("Cumulative Sepal Length")
plt.legend(iris.target_names)
plt.show()

# 2. Bar Chart - Average petal length per species
plt.figure(figsize=(6,4))
sns.barplot(x="species", y="petal length (cm)", data=df, estimator="mean", errorbar=None)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram - Sepal length distribution
plt.figure(figsize=(6,4))
sns.histplot(df["sepal length (cm)"], bins=15, kde=True)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot - Sepal length vs Petal length
plt.figure(figsize=(6,4))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="Set2")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# -------------------------
# Key Findings (printed)
# -------------------------

print("\nKey Findings:")
print("1. Petal measurements differ more strongly between species than sepal measurements.")
print("2. Setosa species has distinctly smaller petal length/width compared to Versicolor and Virginica.")
print("3. Sepal length distribution is fairly normal, with slight variation between species.")
print("4. Scatter plot shows that petal length can clearly separate species groups.")
