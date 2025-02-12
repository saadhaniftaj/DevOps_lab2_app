import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "netflix_titles.csv"  # Ensure the file is in the same directory
try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: Dataset file not found. Ensure 'netflix_titles.csv' is in the same directory.")
    exit()

# Display basic information about the dataset
print("\nDataset Info:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values for visualization purposes
df.fillna("Unknown", inplace=True)

# Plot distribution of TV Shows vs. Movies
plt.figure(figsize=(7, 5))
sns.countplot(x='type', data=df, palette="coolwarm")
plt.title("Count of TV Shows vs. Movies on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# Plot the top 10 countries with the most Netflix content
plt.figure(figsize=(10, 5))
top_countries = df['country'].value_counts().head(10)
sns.barplot(x=top_countries.index, y=top_countries.values, palette="viridis")
plt.xticks(rotation=45)
plt.title("Top 10 Countries with Most Netflix Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()

# Plot the number of releases per year
plt.figure(figsize=(12, 6))
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
sns.histplot(df['release_year'].dropna(), bins=30, kde=True, color="blue")
plt.title("Distribution of Release Years")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

# Display most common genres (listed in 'listed_in' column)
plt.figure(figsize=(10, 5))
top_genres = df['listed_in'].value_counts().head(10)
sns.barplot(y=top_genres.index, x=top_genres.values, palette="magma")
plt.title("Top 10 Most Common Genres on Netflix")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.show()
