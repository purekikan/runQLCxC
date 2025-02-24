import pandas as pd
import matplotlib.pyplot as plt

def plot_investor_demographics():
    # Load dataset from CSV
    df = pd.read_csv("datasets/dealInvestor.csv")

    # Categorize investor regions
    df['Investor Region'] = df['investorCountry'].apply(lambda x: x if x in ['Canada', 'USA'] else 'International')

    # Define custom order
    category_order = ["Canada", "USA", "International"]

    # Count number of investments per region and round type
    investment_counts = df.groupby(['Investor Region', 'roundType']).size().unstack(fill_value=0)

    # Reindex to enforce order
    investment_counts = investment_counts.reindex(category_order)

    # Plot
    investment_counts.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')

    plt.xlabel("Investor Region")
    plt.ylabel("Number of Investments")
    plt.title("Investor Demographics & Behavior")
    plt.legend(title="Round Type")
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Show the plot
    plt.show()

# Run only if executed directly
if __name__ == "__main__":
    plot_investor_demographics()