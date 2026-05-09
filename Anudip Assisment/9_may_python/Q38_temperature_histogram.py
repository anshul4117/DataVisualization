# Q38. Generate random temperature data using NumPy and plot a histogram
#      representing temperature distribution.

import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate random temperature data for 365 days (in Celsius)
# Using normal distribution: mean=28°C, std=8°C (simulating Indian weather)
daily_temperatures = np.random.normal(loc=28, scale=8, size=365)

# Clip temperatures to realistic range (-5 to 50)
daily_temperatures = np.clip(daily_temperatures, -5, 50)

# --- Main Program ---
print("=" * 55)
print("   TEMPERATURE DISTRIBUTION ANALYSIS")
print("=" * 55)

# Display statistics
print("\n--- Temperature Statistics (365 days) ---")
print(f"  Mean Temperature     : {np.mean(daily_temperatures):.2f}°C")
print(f"  Median Temperature   : {np.median(daily_temperatures):.2f}°C")
print(f"  Max Temperature      : {np.max(daily_temperatures):.2f}°C")
print(f"  Min Temperature      : {np.min(daily_temperatures):.2f}°C")
print(f"  Std Deviation        : {np.std(daily_temperatures):.2f}°C")

# Categorize temperatures
cold_days = np.sum(daily_temperatures < 15)
mild_days = np.sum((daily_temperatures >= 15) & (daily_temperatures < 25))
warm_days = np.sum((daily_temperatures >= 25) & (daily_temperatures < 35))
hot_days = np.sum(daily_temperatures >= 35)

print(f"\n--- Day Classification ---")
print(f"  Cold days  (< 15°C)    : {cold_days} days")
print(f"  Mild days  (15-25°C)   : {mild_days} days")
print(f"  Warm days  (25-35°C)   : {warm_days} days")
print(f"  Hot days   (>= 35°C)   : {hot_days} days")

# --- Histogram Plot ---
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Histogram 1: Temperature distribution
colors_hist = '#FF5722'
axes[0].hist(daily_temperatures, bins=25, color=colors_hist, edgecolor='black',
             alpha=0.75, label='Temperature Frequency')

# Add mean and median lines
axes[0].axvline(np.mean(daily_temperatures), color='blue', linestyle='--',
                linewidth=2, label=f'Mean: {np.mean(daily_temperatures):.1f}°C')
axes[0].axvline(np.median(daily_temperatures), color='green', linestyle='-.',
                linewidth=2, label=f'Median: {np.median(daily_temperatures):.1f}°C')

axes[0].set_title("Daily Temperature Distribution (365 Days)", fontsize=14, fontweight='bold')
axes[0].set_xlabel("Temperature (°C)", fontsize=12, fontweight='bold')
axes[0].set_ylabel("Frequency (Number of Days)", fontsize=12, fontweight='bold')
axes[0].legend(fontsize=10)
axes[0].grid(axis='y', alpha=0.3)

# Histogram 2: Categorized bar chart
categories = ['Cold\n(< 15°C)', 'Mild\n(15-25°C)', 'Warm\n(25-35°C)', 'Hot\n(≥ 35°C)']
counts = [cold_days, mild_days, warm_days, hot_days]
bar_colors = ['#2196F3', '#4CAF50', '#FF9800', '#F44336']

bars = axes[1].bar(categories, counts, color=bar_colors, edgecolor='black', width=0.6)
axes[1].set_title("Temperature Category Distribution", fontsize=14, fontweight='bold')
axes[1].set_xlabel("Category", fontsize=12, fontweight='bold')
axes[1].set_ylabel("Number of Days", fontsize=12, fontweight='bold')
axes[1].grid(axis='y', alpha=0.3)

# Add value labels on bars
for bar, count in zip(bars, counts):
    axes[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
                 str(count), ha='center', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig("temperature_histogram.png", dpi=150, bbox_inches='tight')
print("\nHistogram saved as 'temperature_histogram.png'")
plt.show()

# --- Expected Output ---
# =======================================================
#    TEMPERATURE DISTRIBUTION ANALYSIS
# =======================================================
#
# --- Temperature Statistics (365 days) ---
#   Mean Temperature     : 27.86°C
#   Median Temperature   : 27.78°C
#   Max Temperature      : 48.23°C
#   Min Temperature      : 8.45°C
#   Std Deviation        : 7.89°C
#
# --- Day Classification ---
#   Cold days  (< 15°C)    : 18 days
#   Mild days  (15-25°C)   : 107 days
#   Warm days  (25-35°C)   : 170 days
#   Hot days   (>= 35°C)   : 70 days
#
# Histogram saved as 'temperature_histogram.png'
# (Histogram window opens showing temperature distribution)
