import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_deal_trends():
    # Load the dataset
    deals = pd.read_csv("datasets/deals.csv")

    # Filter out missing values
    deals = deals[['roundType', 'amount', 'yearQuarter']].dropna()

    # Ensure 'yearQuarter' has a clean format
    deals['yearQuarter'] = deals['yearQuarter'].astype(str)

    # Aggregate data by year, quarter, and funding stage
    deal_summary = deals.groupby(['yearQuarter', 'roundType']).agg(
        total_deals=('amount', 'count'),  # Total number of deals
        total_funding=('amount', 'sum')  # Total funding amount
    ).reset_index()

    # Pivot data for stacked bar chart
    deals_pivot = deal_summary.pivot(index='yearQuarter', columns='roundType', values='total_deals').fillna(0)
    funding_pivot = deal_summary.pivot(index='yearQuarter', columns='roundType', values='total_funding').fillna(0)

    # Plot Number of Deals
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    deals_pivot.plot(kind='bar', stacked=True, colormap='viridis', ax=axes[0])
    axes[0].set_title("Number of Deals per Stage over Time")
    axes[0].set_xlabel("Year & Quarter")
    axes[0].set_ylabel("Total Number of Deals")

    funding_pivot.plot(kind='bar', stacked=True, colormap='magma', ax=axes[1])
    axes[1].set_title("Total Deal Size per Stage over Time")
    axes[1].set_xlabel("Year & Quarter")
    axes[1].set_ylabel("Total Deal Size (USD)")

    # Improve x-axis formatting
    for ax in axes:
        ax.set_xticks(range(0, len(deals_pivot.index), 4))  # Show every 4th label
        ax.set_xticklabels(deals_pivot.index[::4], rotation=45, ha='right')  # Rotate for better readability
        ax.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

# Run only if executed directly
if __name__ == "__main__":
    analyze_deal_trends()
