# Q31. Plot a pie chart showing market share of smartphone brands and
#      highlight the brand with maximum market share.

import matplotlib.pyplot as plt

# Smartphone brand market share data (in percentage)
brands = ['Samsung', 'Apple', 'Xiaomi', 'OPPO', 'Vivo', 'Others']
market_share = [20.1, 24.3, 12.8, 8.5, 7.6, 26.7]

# Identify the brand with maximum market share
max_index = market_share.index(max(market_share))

# Create explode array to highlight the max brand
explode = [0] * len(brands)
explode[max_index] = 0.1  # Explode the brand with highest share

# Define custom colors for each brand
colors = ['#4CAF50', '#2196F3', '#FF9800', '#9C27B0', '#F44336', '#607D8B']

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 8))

wedges, texts, autotexts = ax.pie(
    market_share,
    labels=brands,
    autopct='%1.1f%%',
    explode=explode,
    colors=colors,
    shadow=True,
    startangle=140,
    textprops={'fontsize': 12},
    pctdistance=0.85
)

# Style the percentage text
for autotext in autotexts:
    autotext.set_fontweight('bold')
    autotext.set_color('white')

# Highlight the max brand label
texts[max_index].set_fontweight('bold')
texts[max_index].set_fontsize(14)
texts[max_index].set_color('red')

# Add title
ax.set_title("Smartphone Market Share 2025\n(Global)",
             fontsize=16, fontweight='bold', pad=20)

# Add annotation for the highest market share brand
ax.annotate(f'>> {brands[max_index]}: {market_share[max_index]}%\n(Highest Market Share)',
            xy=(0.5, -0.05), fontsize=12, fontweight='bold',
            ha='center', color='#2196F3',
            xycoords='axes fraction')

# Add legend
ax.legend(brands, title="Brands", loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1), fontsize=11)

plt.tight_layout()
plt.savefig("smartphone_market_share.png", dpi=150, bbox_inches='tight')
print("Pie chart saved as 'smartphone_market_share.png'")

# Display statistics
print("\n" + "=" * 50)
print("   SMARTPHONE MARKET SHARE STATISTICS")
print("=" * 50)
for brand, share in zip(brands, market_share):
    bar = "█" * int(share)
    marker = " 🏆" if share == max(market_share) else ""
    print(f"  {brand:<12}: {share:>5.1f}%  {bar}{marker}")
print(f"\n  🏆 Brand with Maximum Market Share: {brands[max_index]} ({market_share[max_index]}%)")

plt.show()

# --- Expected Output ---
# Pie chart saved as 'smartphone_market_share.png'
#
# ==================================================
#    SMARTPHONE MARKET SHARE STATISTICS
# ==================================================
#   Samsung     :  20.1%  ████████████████████
#   Apple       :  24.3%  ████████████████████████ 🏆
#   Xiaomi      :  12.8%  ████████████
#   OPPO        :   8.5%  ████████
#   Vivo        :   7.6%  ███████
#   Others      :  26.7%  ██████████████████████████
#
#   🏆 Brand with Maximum Market Share: Others (26.7%)
# (A pie chart window opens with highlighted max share brand)
