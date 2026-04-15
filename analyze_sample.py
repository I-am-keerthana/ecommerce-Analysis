import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("outputs", exist_ok=True)

df = pd.read_csv("sample_data/laptops_sample.csv")

print("=== E-commerce Laptop Analysis ===\n")
print(f"Total products: {len(df)}")
print(f"Brands: {df['brand'].nunique()}")
print(f"Price range: ${df['price_usd'].min()} – ${df['price_usd'].max()}")
print(f"Average rating: {df['rating'].mean():.2f}")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Newegg Laptop Market Analysis", fontsize=15, fontweight="bold")

brand_avg = df.groupby("brand")["price_usd"].mean().sort_values(ascending=False)
axes[0, 0].bar(brand_avg.index, brand_avg.values, color="#4C72B0")
axes[0, 0].set_title("Average price by brand")
axes[0, 0].set_ylabel("Price (USD)")
axes[0, 0].tick_params(axis="x", rotation=45)

axes[0, 1].scatter(df["price_usd"], df["rating"], alpha=0.6, color="#55A868")
axes[0, 1].set_title("Price vs rating")
axes[0, 1].set_xlabel("Price (USD)")
axes[0, 1].set_ylabel("Rating")

ram_counts = df["ram_gb"].value_counts().sort_index()
axes[1, 0].bar(ram_counts.index.astype(str), ram_counts.values, color="#C44E52")
axes[1, 0].set_title("RAM distribution")
axes[1, 0].set_xlabel("RAM (GB)")
axes[1, 0].set_ylabel("Count")

axes[1, 1].hist(df["price_usd"], bins=10, color="#8172B2", edgecolor="white")
axes[1, 1].set_title("Price distribution")
axes[1, 1].set_xlabel("Price (USD)")
axes[1, 1].set_ylabel("Count")

plt.tight_layout()
plt.savefig("outputs/laptop_analysis.png", dpi=150, bbox_inches="tight")
print("\nChart saved to outputs/laptop_analysis.png")
plt.show()
