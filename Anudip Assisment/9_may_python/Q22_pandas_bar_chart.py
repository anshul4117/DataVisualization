# Q22. Read sales data from a CSV file using Pandas and plot a bar chart
#      representing product-wise sales using Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt
import os

def create_sales_csv(filename):
    """Create a sample sales CSV file for demonstration."""
    data = {
        'Product': ['Laptop', 'Mobile', 'Tablet', 'Headphones', 'Smartwatch',
                     'Camera', 'Speaker', 'Keyboard', 'Mouse', 'Monitor'],
        'Q1_Sales': [150, 320, 90, 200, 180, 60, 110, 250, 300, 75],
        'Q2_Sales': [180, 350, 110, 230, 200, 80, 130, 270, 310, 95],
        'Q3_Sales': [200, 400, 130, 260, 220, 100, 150, 290, 330, 110],
        'Q4_Sales': [250, 450, 160, 300, 270, 120, 180, 320, 370, 140]
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"  Sales CSV file '{os.path.basename(filename)}' created successfully!\n")


# --- Main Program ---
print("=" * 60)
print("   PRODUCT-WISE SALES ANALYSIS & BAR CHART")
print("=" * 60)

# Create sample CSV file
csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sales_data.csv")
create_sales_csv(csv_path)

# Read sales data from CSV
sales_df = pd.read_csv(csv_path)

# Display the sales data
print("--- Sales Data ---")
print(sales_df.to_string(index=False))

# Calculate total annual sales per product
sales_df['Total_Sales'] = (sales_df['Q1_Sales'] + sales_df['Q2_Sales'] +
                           sales_df['Q3_Sales'] + sales_df['Q4_Sales'])

# Display total sales
print("\n--- Product-wise Total Sales ---")
for _, row in sales_df.iterrows():
    print(f"  {row['Product']:<15}: {row['Total_Sales']} units")

# --- Bar Chart ---
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Chart 1: Grouped bar chart for quarterly sales
x = range(len(sales_df['Product']))
bar_width = 0.2

axes[0].bar([i - 1.5 * bar_width for i in x], sales_df['Q1_Sales'],
            width=bar_width, label='Q1', color='#4CAF50')
axes[0].bar([i - 0.5 * bar_width for i in x], sales_df['Q2_Sales'],
            width=bar_width, label='Q2', color='#2196F3')
axes[0].bar([i + 0.5 * bar_width for i in x], sales_df['Q3_Sales'],
            width=bar_width, label='Q3', color='#FF9800')
axes[0].bar([i + 1.5 * bar_width for i in x], sales_df['Q4_Sales'],
            width=bar_width, label='Q4', color='#F44336')

axes[0].set_xlabel("Products", fontsize=12, fontweight='bold')
axes[0].set_ylabel("Sales (Units)", fontsize=12, fontweight='bold')
axes[0].set_title("Quarterly Sales by Product", fontsize=14, fontweight='bold')
axes[0].set_xticks(x)
axes[0].set_xticklabels(sales_df['Product'], rotation=45, ha='right')
axes[0].legend()
axes[0].grid(axis='y', alpha=0.3)

# Chart 2: Total sales bar chart
colors = plt.cm.viridis([i / len(sales_df) for i in range(len(sales_df))])
axes[1].bar(sales_df['Product'], sales_df['Total_Sales'], color=colors, edgecolor='black')
axes[1].set_xlabel("Products", fontsize=12, fontweight='bold')
axes[1].set_ylabel("Total Annual Sales (Units)", fontsize=12, fontweight='bold')
axes[1].set_title("Total Annual Sales by Product", fontsize=14, fontweight='bold')
axes[1].tick_params(axis='x', rotation=45)
axes[1].grid(axis='y', alpha=0.3)

# Add value labels on bars
for i, val in enumerate(sales_df['Total_Sales']):
    axes[1].text(i, val + 10, str(val), ha='center', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig("product_sales_chart.png", dpi=150, bbox_inches='tight')
print("\nChart saved as 'product_sales_chart.png'")
plt.show()

# --- Expected Output ---
# ============================================================
#    PRODUCT-WISE SALES ANALYSIS & BAR CHART
# ============================================================
#   Sales CSV file 'sales_data.csv' created successfully!
#
# --- Sales Data ---
#    Product  Q1_Sales  Q2_Sales  Q3_Sales  Q4_Sales
#     Laptop       150       180       200       250
#     Mobile       320       350       400       450
#     ...
#
# --- Product-wise Total Sales ---
#   Laptop         : 780 units
#   Mobile         : 1520 units
#   ...
#
# Chart saved as 'product_sales_chart.png'
# (Bar chart window opens with quarterly and total sales charts)
