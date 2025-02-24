import pandas as pd
import matplotlib.pyplot as plt

def analyze_investment_firms_by_country_and_stage():
    # Load the dataset
    deal_investor = pd.read_csv("datasets/dealInvestor.csv")

    # Clean data
    deal_investor['investorCountry'] = deal_investor['investorCountry'].astype(str).str.strip().str.lower()
    deal_investor['roundType'] = deal_investor['roundType'].astype(str).str.strip()

    # Filter data to remove NaNs
    deal_investor = deal_investor.dropna(subset=['investorCountry', 'roundType'])

    # Re-categorize countries into 'Canada', 'USA', 'International'
    def categorize_country(country):
        country = country.strip().lower()
        if country == 'canada':
            return 'Canada'
        elif country == 'usa' or country == 'united states':
            return 'USA'
        else:
            return 'International'

    deal_investor['investorCountry'] = deal_investor['investorCountry'].apply(categorize_country)

    # Group by country and funding stage, and count distinct investment firms
    investment_count = deal_investor.groupby(['investorCountry', 'roundType']).agg(
        num_investment_firms=('investorName', 'nunique')
    ).reset_index()

    # Pivot the data for stacked bar chart (countries on x-axis, funding stages on columns)
    pivot_data = investment_count.pivot_table(
        index='investorCountry',
        columns='roundType',
        values='num_investment_firms',
        aggfunc='sum',
        fill_value=0
    )

    # Re-order the x-axis to have Canada, USA, and International
    pivot_data = pivot_data.loc[['Canada', 'USA', 'International']]

    # Plot the stacked bar chart
    pivot_data.plot(kind='bar', stacked=True, figsize=(14, 10), colormap="viridis")

    # Customize plot
    plt.title("Number of Investment Firms per Funding Stage by Country")
    plt.xlabel("Countries")
    plt.ylabel("Number of Investment Firms")
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.legend(title="Funding Stages", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.subplots_adjust(bottom=0.3, right=0.8)  # Adjust layout
    plt.show()

# Run only if executed directly
if __name__ == "__main__":
    analyze_investment_firms_by_country_and_stage()
