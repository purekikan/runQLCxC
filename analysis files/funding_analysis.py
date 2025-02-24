import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.metrics.distance import edit_distance

matplotlib.use("TkAgg")  # Set the backend to TkAgg

# Define sector groups
sectorGroup = {
    'Technology and Software': [
       'SaaS', 'Quantum', 'Wearables', 'Robotics', 'Metaverse', 'ioT', 'Networks', 'blockchain', 'HRTech', 'AR', 'Electronics', 'BatteryTech',
        '3DTech', 'Platform', 'PaaS', 'DevTech', 'GeoTech', 'Hardware', 'Application Software', 'API', 'Enterprise Software',
      'HCI', 'VR', 'Biometrics', 'VisionTech', 'DisplayTech', 'NoCode',
        '3D Printing', 'Software Development', 'Computers and Electronics Manu', 'Desktop Computing Software Pro', 'Imaging'],
    'Data and Information System': [
       'AI',  'Analytics', 'Data', 'Cloud Computing', 'Machine Learning', 'Artificial Intelligences', 'information technology',
        'Email', 'GeoSpatial', 'data analysis', 'information technology , Trade', 'Technology, Information, Inter', 'Technology, Information and In'
    ],
    'Health and Biotech': [
        'BioTech', 'Pharmaceutical', 'Medical', 'Health Care Services', 'Electronic Health Record (EHR)', 'Health Diagnostics', 'Hospitals and Health Care',
        'MedTech', 'HealthTech', 'Pharmaceutical Manufacturing', 'Medical Device', 'Medical Equipment Manufacturin', 'Biotechnology Research',
        'Biotechnology', 'Womens Health', 'WellnessTech'
    ],
    'Finance, Business, and Marketing': [
        'FinTech', 'InsurTech', 'Cryptocurrency', 'B2B', 'Payments', 'Marketing', 'Recruiting', 'Career Planning', 'Billing', 'eCommerce', 'Marketplace', 'SalesTech', 'CRM', 'RetailTech', 'DeFi', 'ERP', 'financial services', 'insurance software', 'Retail', 'MarTech', 'Consumer', 'CrowdFunding', 'retail recyclable materials &'
    ],
    'Environment and Agriculture': [
        'CleanTech', 'AgrTech', 'agTech', 'GreenTech', 'Environmental', 'Energy Efficiency', 'Renewable Energy', 'Mining Technology',
        'Environmental Services', 'Animal Feed Manufacturing', 'Chemical Raw Materials Manufac', 'ag-tech', 'FoodTech'
    ],
    'Media, Communications, and Entertainment': [
        'Media', 'eSports', 'Online Audio and Video Media', 'VideoTech', 'Mobile', 'AudioTech', 'Telecommunications', 'Communications Infrastructure', 'eLearning', 'Social', 'EntertainmentTech', 'SocialTech', 'Games'
    ],
    'Services and Security': [
        'Cybersecurity', 'Security and Investigations', 'GovTech', 'LegalTech', 'Consulting', 'R&D', 'FitnessTech', 'EdTech'
    ],
    'Engineering, and Construction': [
        'Civil Engineering', 'ContructionTech', 'Construction Software', 'Automation Machinery Manufactu', 'Manufacturing',
        'Industrial Automation', 'Industrial Machinery Manufactu', 'Real Estate', 'Automotive', 'PropertyTech'
    ],
    'Travel and Logistics': [
        'LogisticsTech', 'TransportationTech', 'Last Mile Transportation', 'Maritime Transportation', 'Rail Transportation', 'AutoTech',
        'Logistics', 'TravelTech', 'Aerospace', 'SpaceTech'
    ],
    'Others': [
        'Misc', 'NanoTech', 'AdTech', 'PetTech', 'SportsTech', 'Electrochromic', 'Esphera SynBio'
    ]
}

# Convert sector group tags to lowercase
sectorGroup = {key: [tag.lower() for tag in value] for key, value in sectorGroup.items()}


def assign_group(primary_tag):
    for group, tags in sectorGroup.items():
        if primary_tag in tags:
            return group
    return 'Others'  # Default group


def analyze_funding_stages():
    # Load the dataset
    deals = pd.read_csv("datasets/deals.csv")

    # Clean and normalize sector names
    deals['primaryTag'] = deals['primaryTag'].astype(str).str.lower().str.strip()

    # Drop empty (NaN) tags to avoid errors
    deals = deals[deals['primaryTag'].notna()]

    # Fuzzy matching for similar tags
    unique_tags = deals['primaryTag'].dropna().unique()
    tag_mapping = {}

    for i, tag1 in enumerate(unique_tags):
        if pd.isna(tag1):  # Skip NaN values
            continue

        tag1 = str(tag1)  # Ensure tag1 is a string
        if tag1 in tag_mapping:
            continue  # Skip already mapped tags

        tag_mapping[tag1] = tag1  # Initialize mapping with itself
        for tag2 in unique_tags[i + 1:]:
            if pd.isna(tag2):  # Skip NaN values
                continue

            tag2 = str(tag2)  # Ensure tag2 is a string
            if tag2 not in tag_mapping:  # Check if the tag has been assigned
                if (edit_distance(tag1, tag2) <= 2 and len(tag1) >= 10) or (
                        edit_distance(tag1, tag2) <= 1 and len(tag1) >= 8):
                    tag_mapping[tag2] = tag1  # Assign similar tag

    # Apply mapping
    deals['primaryTag'] = deals['primaryTag'].map(tag_mapping)

    # Assign sector groups
    deals['sectorGroup'] = deals['primaryTag'].apply(assign_group)

    # Filter out missing values
    deals = deals[['roundType', 'amount', 'sectorGroup']].dropna()

    # Convert 'amount' column to numeric, handling errors
    deals['amount'] = pd.to_numeric(deals['amount'], errors='coerce')

    # Aggregate: Total number of deals & total funding volume per sector and stage
    funding_summary = deals.groupby(['sectorGroup', 'roundType']).agg(
        total_deals=('amount', 'count'),  # Number of deals
        total_funding=('amount', 'sum')  # Total funding amount
    ).reset_index()

    # Pivot data for plotting
    pivot_deals = funding_summary.pivot(index='sectorGroup', columns='roundType', values='total_deals').fillna(0)

    # Plot
    pivot_deals.plot(kind='bar', stacked=True, figsize=(14, 10), colormap="viridis")
    plt.title("Number of Deals per Sector Group by Funding Stage")
    plt.xlabel("Sector Groups")
    plt.ylabel("Number of Deals")
    plt.legend(title="Funding Stage", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=90, fontsize=7)
    plt.subplots_adjust(bottom=0.3, right=0.8)  # Adjust layout
    plt.show()


# Run only if executed directly
if __name__ == "__main__":
    analyze_funding_stages()
