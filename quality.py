import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Data extracted from your report (averaged values per hall)
data = {
    "Hall": ["Mellanby", "Tedder", "Kuti", "Sultan Bello", "Zik", "Independence"],
    "pH": [5.47, 6.64, 6.33, 6.00, 6.39, 6.03],
    "Temperature": [29.37, 29.47, 29.83, 29.43, 29.3, 29.17],
    "Conductivity": [3.71, 4.69, 4.18, 3.65, 4.49, 3.34],
    "TDS": [103.3, 146.7, 143.3, 110, 163.3, 100],
    "Turbidity": [3.4, 2.57, 3.45, 2.46, 3.84, 4.09],
    "Total Hardness": [96.67, 160.67, 160.67, 118.67, 163.33, 93.33],
    "Total Alkalinity": [94.67, 196.67, 183, 129.33, 163.33, 93.33],
    "Total Chloride": [71.33, 39.67, 46.67, 57.33, 77.67, 57],
    "Chlorine": [0.42, 0.52, 0.52, 0.56, 0.4, 0.7],
    "Nitrate": [3.14, 2.84, 2.83, 2.98, 2.05, 2.95],
    "Sulphate": [0.18, 0.6, 0.6, 0.54, 0.76, 0.54],
    "Magnesium": [0.21, 45, 45, 28.67, 50, 25.67],
    "Potassium": [0.053, 0.2, 0.2, 0.213, 0.257, 0.313],
    "Sodium": [0.03, 0.053, 0.053, 0.073, 0.1, 0.073],
    "Total Coliform": [3.33, 538.67, 538.67, 534.67, 534, 801.33],
    "E. Coli": [2, 275.33, 275.33, 355.67, 187.33, 720.67]
}

# Convert to DataFrame
df = pd.DataFrame(data)
df.set_index("Hall", inplace=True)

# Compute correlation matrix
correlation_matrix = df.corr()

# Identify highest and lowest correlations
strongest_corr = correlation_matrix.unstack().sort_values(ascending=False)
strongest_corr = strongest_corr[strongest_corr < 1]  # Remove self-correlations

# Display top 5 strongest positive and negative correlations
print("Top 5 Strongest Positive Correlations:")
print(strongest_corr.head(5))

print("\nTop 5 Strongest Negative Correlations:")
print(strongest_corr.tail(5))

# Generate heatmap for visualization
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap of Water Quality Parameters")
plt.show()

