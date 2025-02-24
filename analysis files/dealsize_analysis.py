import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.use("TkAgg")  # Set the backend to TkAgg

def analyze_deal_size_evolution():
    # Load the dataset
    deals = pd.read_csv("datasets/deals.csv")

    # Ensure 'date' column is in datetime format (Modify column name if necessary)
    deals['date'] = pd.to_datetime(deals['date'])

    # Extract the quarter (format: YYYY-Q#)
    deals['quarter'] = deals['date'].dt.to_period('Q').astype(str)

    # Filter necessary columns
    deals = deals[['quarter', 'roundType', 'amount']].dropna()

    # Calculate average deal size per funding stage per quarter
    avg_deal_size = deals.groupby(['quarter', 'roundType'])['amount'].mean().reset_index()

    # Plot using Seaborn
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=avg_deal_size, x='quarter', y='amount', hue='roundType', marker='o', palette='viridis')

    # Customize the plot
    plt.title("Average Deal Size per Funding Stage Over Time")
    plt.xlabel("Quarter")
    plt.ylabel("Average Deal Size (USD)")
    plt.xticks(rotation=45, fontsize=8)  # Adjust rotation and font size
    plt.legend(title="Funding Stage", loc="best")
    plt.grid(True)

    plt.show()


# Run only if executed directly
if __name__ == "__main__":
    analyze_deal_size_evolution()
