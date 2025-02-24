import pandas as pd
import plotly.express as px
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import base64
from io import BytesIO

def dealsVolume_sectorGroup_fundingStages(data_path, options = []):
    pivot_deals = pd.read_csv(data_path)
    pivot_deals.set_index('sectorGroup', inplace=True)
    fig = plt.figure(figsize=(14, 10))
    categories = list(pivot_deals.index)
    bottom = [0] * len(categories)
    colormap = cm.get_cmap('viridis', len(pivot_deals.columns))


    for i in range(len(pivot_deals.columns)):
        plt.bar(categories, pivot_deals[pivot_deals.columns[i]], bottom=bottom, label=pivot_deals.columns[i], color=colormap(i))
        bottom = [sum(x) for x in zip(bottom, pivot_deals[pivot_deals.columns[i]])]
    plt.title("Number of Deals per Sector Group by Funding Stage")
    plt.xlabel("Sector Groups")
    plt.ylabel("Number of Deals")
    plt.legend(title="Funding Stage", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45, fontsize=7)
    plt.subplots_adjust(bottom=0.3, right=0.8)  # Adjust layout
    plt.tight_layout()
    
    buf = BytesIO()
    fig.savefig(buf, format="png")
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

    return fig_bar_matplotlib

def dealSize_fundingStage_time(data_path, options = []):
    avg_deal_size = pd.read_csv(data_path)
    fig = plt.figure(figsize=(12, 6))
    sns.lineplot(data=avg_deal_size, x='quarter', y='amount', hue='roundType', marker='o', palette='viridis')

    # Customize the plot
    plt.title("Average Deal Size per Funding Stage Over Time")
    plt.xlabel("Quarter")
    plt.ylabel("Average Deal Size (USD)")
    plt.xticks(rotation=45, fontsize=8)  # Adjust rotation and font size
    plt.legend(title="Funding Stage", loc="best")
    plt.grid(True)
    plt.tight_layout()
        
    buf = BytesIO()
    fig.savefig(buf, format="png")
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

    return fig_bar_matplotlib

def dealSize_fundingStage_time_bar(data_path, options = []):
    deals_pivot = pd.read_csv(data_path)
    deals_pivot.set_index('yearQuarter', inplace=True)
    #fig = plt.figure(figsize=(14, 10))

    deals_pivot.plot(kind='bar', stacked=True, colormap='viridis', figsize=(14, 10))
    plt.title(f"{options[0]} per Stage over Time")
    plt.xlabel("Year & Quarter")
    plt.ylabel(f"Total {options[0]}")

    plt.xticks(range(0, len(deals_pivot.index), 4), deals_pivot.index[::4], rotation=45, ha='right')  # Rotate for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format="png")
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

    return fig_bar_matplotlib
