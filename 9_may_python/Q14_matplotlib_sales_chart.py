# Q14. Line chart using Matplotlib to display monthly sales data
#      with title, labels, legend, and grid.

import matplotlib.pyplot as plt

# Monthly sales data for a company
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Sales data for two years (in thousands)
sales_2024 = [45, 52, 48, 61, 55, 67, 72, 69, 75, 80, 85, 95]
sales_2025 = [50, 58, 55, 68, 63, 74, 78, 82, 88, 92, 98, 110]

# Create figure and axis with specified size
fig, ax = plt.subplots(figsize=(12, 6))

# Plot line chart for 2024 sales
ax.plot(months, sales_2024, marker='o', linewidth=2, markersize=8,
        color='#2196F3', label='Sales 2024', linestyle='-')

# Plot line chart for 2025 sales
ax.plot(months, sales_2025, marker='s', linewidth=2, markersize=8,
        color='#FF5722', label='Sales 2025', linestyle='--')

# Add title and labels
ax.set_title("Monthly Sales Data - Company XYZ", fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel("Months", fontsize=13, fontweight='bold')
ax.set_ylabel("Sales (in Thousands Rs.)", fontsize=13, fontweight='bold')

# Add legend
ax.legend(loc='upper left', fontsize=11, framealpha=0.9)

# Add grid for better visualization
ax.grid(True, linestyle='--', alpha=0.7)

# Annotate the highest sales point for 2025
max_sales_index = sales_2025.index(max(sales_2025))
ax.annotate(f'Peak: {max(sales_2025)}K',
            xy=(months[max_sales_index], max(sales_2025)),
            xytext=(months[max_sales_index - 2], max(sales_2025) + 5),
            arrowprops=dict(arrowstyle='->', color='red'),
            fontsize=10, color='red', fontweight='bold')

# Set y-axis limits for better display
ax.set_ylim(30, 120)

# Add a subtle background color
ax.set_facecolor('#f8f9fa')

# Tight layout to prevent label cutoff
plt.tight_layout()

# Save the chart
plt.savefig("monthly_sales_chart.png", dpi=150, bbox_inches='tight')
print("Chart saved as 'monthly_sales_chart.png'")

# Display the chart
plt.show()

# --- Expected Output ---
# Chart saved as 'monthly_sales_chart.png'
# (A line chart window will open showing:)
# - Title: "Monthly Sales Data - Company XYZ"
# - X-axis: Months (Jan to Dec)
# - Y-axis: Sales in Thousands Rs.
# - Two lines: Blue solid line for 2024, Red dashed line for 2025
# - Grid lines for easy reading
# - Legend in upper left corner
# - Annotation showing peak sales point
