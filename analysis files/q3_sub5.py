import pandas as pd
import matplotlib.pyplot as plt


def plot_investment_firm_activity():
    # Load dataset
    df = pd.read_csv("datasets/dealInvestor.csv")

    # Count number of deals per investment firm per quarter
    firm_activity = df.groupby(["investorName", "yearQuarter"]).size().unstack(fill_value=0)

    # Select top 10 most active firms (by total number of deals)
    top_firms = firm_activity.sum(axis=1).nlargest(10).index
    firm_activity = firm_activity.loc[top_firms]

    # Plot
    plt.figure(figsize=(12, 6))
    for firm in firm_activity.index:
        plt.plot(firm_activity.columns, firm_activity.loc[firm], marker='o', label=firm)

    plt.xlabel("Quarter")
    plt.ylabel("Number of Deals")
    plt.title("Most Active Investment Firms by Yearly Activity")
    plt.legend(title="Investment Firms", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Show the plot
    plt.tight_layout()
    plt.show()


# Run only if executed directly
if __name__ == "__main__":
    plot_investment_firm_activity()
