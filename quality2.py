import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# WHO Standards for Water Quality Parameters
who_standards = {
    "Total Hardness": 200, "Total Alkalinity": 200, "Total Chloride": 250, 
    "Calcium": 75, "Chlorine": 0.5, "Nitrate": 50, "Sulphate": 250, 
    "Magnesium": 50, "Potassium": 10, "Sodium": 200, "Lead": 0.01, "Iron": 0.3,
    "pH": 6.5, "Temperature": 25, "Turbidity": 5, "Conductivity": 1500, "TDS": 600,
    "E. coli": 0, "Total Coliform": 0
}

# Water Quality Data
water_quality = {
    "Hall": ["Mellanby", "Tedder", "Kuti", "Sultan Bello", "Zik", "Independence"],
    "pH": [5.47, 6.64, 6.33, 6.00, 6.39, 6.03],
    "Temperature": [29.37, 29.47, 29.83, 29.43, 29.3, 29.17],
    "Conductivity": [3.71, 4.69, 4.18, 3.65, 4.49, 3.34],
    "TDS": [103.3, 146.7, 143.3, 110, 163.3, 100],
    "Turbidity": [3.4, 2.57, 3.45, 2.46, 3.84, 4.09],
    "Total Hardness": [96.67, 160.67, 160.67, 118.67, 163.33, 93.33],
    "Total Alkalinity": [94.67, 196.67, 183, 129.33, 163.33, 93.33],
    "Total Chloride": [71.33, 39.67, 46.67, 57.33, 77.67, 57],
    "Calcium": [50, 60, 55, 40, 70, 65],
    "Chlorine": [0.42, 0.52, 0.52, 0.56, 0.4, 0.7],
    "Nitrate": [3.14, 2.84, 2.83, 2.98, 2.05, 2.95],
    "Sulphate": [0.18, 0.6, 0.6, 0.54, 0.76, 0.54],
    "Magnesium": [0.21, 45, 45, 28.67, 50, 25.67],
    "Potassium": [0.053, 0.2, 0.2, 0.213, 0.257, 0.313],
    "Sodium": [0.03, 0.053, 0.053, 0.073, 0.1, 0.073],
    "Lead": [0.005, 0.008, 0.006, 0.007, 0.004, 0.009],
    "Iron": [0.1, 0.2, 0.15, 0.12, 0.25, 0.18],
    "Total Coliform": [3.33, 538.67, 538.67, 534.67, 534, 801.33],
    "E. coli": [2, 275.33, 275.33, 355.67, 187.33, 720.67]
}

# Convert to DataFrame
df = pd.DataFrame(water_quality)
df.set_index("Hall", inplace=True)


# Compute deviation from WHO standards
for param, standard in who_standards.items():
    df[f"{param} Deviation"] = df[param] - standard

# Save the deviations to an Excel file
df_deviation = df[[col for col in df.columns if "Deviation" in col]]
df_deviation.to_excel("Water_Quality_Deviation.xlsx", sheet_name="Deviation Analysis")

print("Deviation values saved as 'Water_Quality_Deviation.xlsx'.")

# Compute correlation matrix for deviations
deviation_columns = [col for col in df.columns if "Deviation" in col]
correlation_matrix = df[deviation_columns].corr()

# Save correlation matrix to Excel
df[deviation_columns].corr().to_excel("Deviation_Correlation.xlsx", sheet_name="Correlation Analysis")

print("Deviation correlation analysis completed. Results saved as 'Deviation_Correlation.xlsx'.")

# Extract deviation data
deviation_columns = [col for col in df.columns if "Deviation" in col]
df_deviation = df[deviation_columns]

# Generate heatmap for visualization
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.xlabel("Hall of Residence")
plt.ylabel("Deviation from WHO Standard")
plt.title("Correlation Heatmap of Deviation from WHO Standards")
plt.show()

# Plot grouped bar chart
plt.figure(figsize=(12, 6))
df_deviation.plot(kind="bar", colormap="coolwarm", figsize=(12, 6))
plt.axhline(y=0, color="black", linestyle="--")  # Reference line for WHO standard
plt.xlabel("Hall of Residence")
plt.ylabel("Deviation from WHO Standard")
plt.title("Deviation of Water Quality Parameters from WHO Standards")
plt.xticks(rotation=45)
plt.legend(loc="upper left", bbox_to_anchor=(1,1))
plt.show()