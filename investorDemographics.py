import pandas as pd
import plotly.express as px
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

def plot_dealsCount_investorRegion(data_path, options = []):
    investment_counts = pd.read_csv(data_path)
    investment_counts.set_index('Investor Region', inplace=True)
    
    investment_counts.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')

    plt.xlabel("Investor Region")
    plt.ylabel("Number of Investments")
    plt.title("Investor Demographics & Behavior")
    plt.legend(title="Round Type")
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    buf = BytesIO()
    plt.savefig(buf, format="png")
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

    return fig_bar_matplotlib

def plot_dealSize_investorRegion(data_path, options = []):
    pivot_data = pd.read_csv(data_path)
    pivot_data.set_index('roundType', inplace=True)
    pivot_data.plot(kind='bar', figsize=(14, 10), colormap="viridis")

    # Customize plot
    plt.title("Average Deal Size per Funding Stage by Investor Geography (USD)")
    plt.xlabel("Funding Stages")
    plt.ylabel("Average Deal Size")
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.legend(title="Investor Geography", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.subplots_adjust(bottom=0.3, right=0.8)  # Adjust layout
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

    return fig_bar_matplotlib

def plot_investor_count_country_funding_stage(data_path, options = []):
    investor_count = pd.read_csv(data_path)
    investor_count.set_index('investorCountry', inplace=True)

    # Plot the stacked bar chart
    investor_count.plot(kind='bar', stacked=True, figsize=(14, 10), colormap="viridis")

    # Customize plot
    plt.title("Number of Investment Firms per Funding Stage by Country")
    plt.xlabel("Countries")
    plt.ylabel("Number of Investment Firms")
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.legend(title="Funding Stages", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.subplots_adjust(bottom=0.3, right=0.8)  # Adjust layout
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

    return fig_bar_matplotlib

def plot_topFirms_quarter(data_path, options = []):
    firm_activity = pd.read_csv(data_path)
    firm_activity.set_index('investorName', inplace=True)

    fig = plt.figure(figsize=(12, 6))
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

    buf = BytesIO()
    plt.savefig(buf, format="png")
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

    return fig_bar_matplotlib

