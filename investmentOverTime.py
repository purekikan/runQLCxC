import pandas as pd
import plotly.express as px
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

def plot_investment_over_time(data_path, options = []):
    transformed_df = pd.read_csv(data_path)
    fig = plt.figure(figsize=(12, 6))
    for column in transformed_df.columns:
        if column != 'year':  # Skip the 'year' column
            plt.plot(transformed_df['year'], transformed_df[column]/10**8, label=column)

    plt.xlabel('Year')
    plt.ylabel('Amount (100 million USD)')
    plt.title('Investment Trends Over Time')
    plt.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=5) #Move legend to bottom
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format="png")
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

    return fig_bar_matplotlib

def plot_deal_size_distribution(data_path, options = []):
    deals_data = pd.read_csv(data_path)
    fig = plt.figure(figsize=(12, 6))
    sns.boxplot(x='year', y='amount', data=deals_data[['year','amount']])
    plt.yscale('log')
    plt.xlabel('Year')
    plt.ylabel('Amount (USD)')
    plt.title('Distribution of Deal Amount by Year (Log Scale)')
    
    buf = BytesIO()
    fig.savefig(buf, format="png")
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

    return fig_bar_matplotlib

def plot_deal_vol_trends_over_time(data_path, options = []):
    data = pd.read_csv(data_path)
    fig = plt.figure(figsize=(10, 6))

    # Data for the stacked bar chart
    categories = data["yearQuarter"]
    values = [data["< 100k"],
                data["100k - 1M"],
                data["1M-5M"],
                data["5M-10M"],
                data["10M-100M"],
                data["> 100M"]]
    labels = ["< 100k", "100k - 1M", "1M-5M", "5M-10M", "10M-100M", "> 100M"]

    # Plot the stacked bar chart
    bottom = [0] * len(categories)
    for i in range(len(values)):
        plt.bar(categories, values[i], bottom=bottom, label=labels[i])
        bottom = [sum(x) for x in zip(bottom, values[i])]
    plt.xlabel('Year')
    plt.ylabel('Number of Deals')
    plt.title('Number of Deals by Year and Deal Amount Group')
    plt.legend(title='Deal Amount Group')
    plt.xticks(rotation=45, ha = 'right')  # Keep x-axis labels horizontal
    plt.tight_layout()
    
    buf = BytesIO()
    fig.savefig(buf, format="png")
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

    return fig_bar_matplotlib

def plot_deal_size_grouping_over_time(data_path, options = [2022]):
    year = options[0]
    data = pd.read_csv(data_path)
    data = data.set_index(['year', 'group'])
    year_data = data.loc[year]
    year_data.reset_index(inplace=True)
    year_data.drop('year', axis=1, inplace=True)
    year_data = year_data.set_index('group')
    # Create the heatmap
    fig = plt.figure(figsize=(12, 6))
    sns.heatmap(year_data, annot=True, cmap='viridis')
    plt.title(f'Deal Amount Group Count by Sector Group in {year}')
    plt.xlabel('Deal Amount Group')
    plt.ylabel('Sector Group')

    buf = BytesIO()
    fig.savefig(buf, format="png")
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

    return fig_bar_matplotlib
