import pandas as pd
import plotly.express as px
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO


def plot_top_sectors(data_path, options = ['Sum']):
    agg = options[0]
    amount_stats_by_tags = pd.read_csv(data_path)
    amount_stats_by_tags.set_index('primaryTag', inplace=True)
    top_tags_by_amount = amount_stats_by_tags[agg.lower()].sort_values(ascending=False).head(25)

    fig = plt.figure(figsize=(10, 6))
    top_tags_by_amount.plot(kind='barh')
    plt.xlabel(f'{agg} of Investment Amount')
    plt.ylabel('Primary Tag')
    plt.title(f'Top Primary Tags by {agg} Amount')
    plt.tight_layout()
    plt.show()

    buf = BytesIO()
    fig.savefig(buf, format="png")
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

    return fig_bar_matplotlib

def plot_top_sectors_group(data_path, options = ['Sum']):
    agg = options[0]
    amount_stats_by_sector_group = pd.read_csv(data_path)
    amount_stats_by_sector_group.set_index('group', inplace=True)
    top_sector_group_by_amount = amount_stats_by_sector_group[agg.lower()].sort_values(ascending=False).head(25)
    
    fig = plt.figure(figsize=(10, 6))
    top_sector_group_by_amount.plot(kind='barh')
    plt.xlabel(f'{agg} of Investment Amount')
    plt.ylabel('Sector Group')
    plt.title(f'Top Sector Group by {agg} Amount')
    plt.tight_layout()
    plt.show()

    buf = BytesIO()
    fig.savefig(buf, format="png")
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

    return fig_bar_matplotlib

def plot_top_ecosystems(data_path, options = ['Sum']):
    agg = options[0]
    amount_stats_by_ecosystem = pd.read_csv(data_path)
    amount_stats_by_ecosystem.set_index('ecosystemName', inplace=True)
    top_ecosystem_by_amount = amount_stats_by_ecosystem[agg.lower()].sort_values(ascending=False).head(25)

    fig = plt.figure(figsize=(10, 6))
    top_ecosystem_by_amount.plot(kind='barh')
    plt.xlabel(f'{agg} of Investment Amount')
    plt.ylabel('Region')
    plt.title(f'Top Region by {agg} Amount')
    plt.tight_layout()
    plt.show()

    buf = BytesIO()
    fig.savefig(buf, format="png")
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

    return fig_bar_matplotlib

def plot_investment_by_ecosystems_over_time(data_path, options = ['year']):
    investment_trends = pd.read_csv(data_path)
    investment_trends.set_index(options[0], inplace=True)
    investment_trends.fillna(0, inplace=True)

    fig = plt.figure(figsize=(12, 6))
    categories = list(investment_trends.index)
    bottom = [0] * len(categories)
    #investment_trends.plot(kind='bar', stacked=True, figsize=(12, 6))
    for i in range(len(investment_trends.columns)):
        plt.bar(categories, investment_trends[investment_trends.columns[i]]/(10**9), bottom=bottom, label=investment_trends.columns[i])
        bottom = [sum(x) for x in zip(bottom, investment_trends[investment_trends.columns[i]]/(10**9))]
    
    plt.xlabel('Year Quarter')
    plt.ylabel('Total Investment Amount (in Billion USD)')
    plt.title('Stacked Bar Chart of Investment Amount by Ecosystem and Time Period')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Ecosystem')
    plt.tight_layout()
    
    buf = BytesIO()
    fig.savefig(buf, format="png")
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

    return fig_bar_matplotlib

def plot_tree_map(data_path, options = ['Sum']):
    ecosystem_sector_investment = pd.read_csv(data_path)
    fig = px.treemap(ecosystem_sector_investment,
                 path=['ecosystemName', 'group'],
                 values='amount',
                 title='Ecosystem and Sector Investment Treemap')
    
    return [None, fig]

def plot_region_heatmap(data_path, options = []):
    heatmap_data = pd.read_csv(data_path)
    heatmap_data.set_index('ecosystemName', inplace=True)
    heatmap_data.fillna(0, inplace=True)
    heatmap_data = heatmap_data.div((10**8))

    fig = plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, annot=False, fmt=".1f", cmap="YlGnBu")  # Adjust fmt and cmap as needed
    plt.title('Investment Amount by Region and Time (100 Million USD)')
    plt.xlabel('Time Period (Year Quarter)')
    plt.ylabel('Ecosystem')

    buf = BytesIO()
    fig.savefig(buf, format="png")
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_heatmap_matplotlib = f'data:image/png;base64,{fig_data}'

    return fig_heatmap_matplotlib