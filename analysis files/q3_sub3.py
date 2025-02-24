import pandas as pd
import matplotlib.pyplot as plt

def analyze_avg_deal_size_by_stage_and_geography():
    # Load the dataset
    deal_investor = pd.read_csv("datasets/dealInvestor.csv")
    deals = pd.read_csv("datasets/deals.csv")

    # Clean column names by stripping any leading/trailing spaces
    deal_investor.columns = deal_investor.columns.str.strip()
    deals.columns = deals.columns.str.strip()

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

    # Merge with deals dataset to get the deal amounts
    deal_investor = deal_investor.merge(deals[['companyName', 'roundType', 'amount']], on='companyName')

    # Fix duplicate 'roundType' columns after merge (rename 'roundType_x' to 'roundType' and drop 'roundType_y')
    deal_investor = deal_investor.rename(columns={'roundType_x': 'roundType'}).drop(columns=['roundType_y'])

    # Check again after merge if 'roundType' is available
    print("Columns after merge:", deal_investor.columns)

    # Group by country, funding stage and calculate the average deal size
    avg_deal_size = deal_investor.groupby(['investorCountry', 'roundType']).agg(
        avg_deal_size=('amount', 'mean')
    ).reset_index()

    # Pivot the data for grouped bar chart (funding stages on x-axis, countries as groups)
    pivot_data = avg_deal_size.pivot_table(
        index='roundType',
        columns='investorCountry',
        values='avg_deal_size',
        aggfunc='mean',
        fill_value=0
    )

    # Plot the grouped bar chart
    pivot_data.plot(kind='bar', figsize=(14, 10), colormap="viridis")

    # Customize plot
    plt.title("Average Deal Size per Funding Stage by Investor Geography (USD)")
    plt.xlabel("Funding Stages")
    plt.ylabel("Average Deal Size")
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.legend(title="Investor Geography", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.subplots_adjust(bottom=0.3, right=0.8)  # Adjust layout
    plt.show()

# Run only if executed directly
if __name__ == "__main__":
    analyze_avg_deal_size_by_stage_and_geography()
