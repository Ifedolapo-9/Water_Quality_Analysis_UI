import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data (Replace with actual values)
data = {
    "Hall": ["Mellanby", "Tedder", "Kuti", "Sultan Bello", "Nnamdi Azikiwe", "Independence"],
    "Water Demand (L)": [26160, 27590, 27790, 22690, 46620, 45840],
    "Storage Capacity (L)": [42500, 52000, 62800, 42200, 131900, 100200]
}

df = pd.DataFrame(data)

# Plot grouped bar chart
plt.figure(figsize=(11,14))
df.plot(x="Hall", kind="bar", stacked=False, figsize=(10,6), colormap="coolwarm")
plt.xlabel("Hall of Residence")
plt.ylabel("Liters")
plt.title("Water Demand vs. Storage Capacity per Hall")
plt.legend(title="Category")
plt.xticks(rotation=45)
plt.show()