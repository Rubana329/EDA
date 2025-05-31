import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (download Titanic dataset from Kaggle and place in same directory)
df = pd.read_csv('titanic.csv')

# Display first few rows
print(df.head())
