# TODO : Add functions to plot all options
from investmentOverTime import *
from sectorAndRegion import *
from fundingStagesAnalysis import *
from investorDemographics import *

#{ Task : { Subtask : { Option : [function, data_path, *args]} } }

key_areas = {
    'Investment Over Time' : {
        'Total Tech Investment over Time' : {
            'Yearly' : [plot_investment_over_time, 'transformed_df_yearly.csv'],
            'Quarterly' : [plot_investment_over_time, 'transformed_df_quarterly.csv']
            }, 
        'Deal Size Distribution per Year' : {
            'Default' : [plot_deal_size_distribution, 'amount_distribution_by_year.csv']
        },
        'Deal Volume Trends over Time' : {
            'Yearly' : [plot_deal_vol_trends_over_time, 'deals_amount_group_count_by_year.csv'],
            'Quarterly' : [plot_deal_vol_trends_over_time,'deals_amount_group_count_by_quarter.csv']
        },
        'Deal Size Grouping over Time' : {
            '2019' : [plot_deal_size_grouping_over_time, 'yearly_sector_group-amount_group_heatmap_data.csv', 2019],
            '2020' : [plot_deal_size_grouping_over_time, 'yearly_sector_group-amount_group_heatmap_data.csv', 2020],
            '2021' : [plot_deal_size_grouping_over_time, 'yearly_sector_group-amount_group_heatmap_data.csv', 2021],
            '2022' : [plot_deal_size_grouping_over_time, 'yearly_sector_group-amount_group_heatmap_data.csv', 2022],
            '2023' : [plot_deal_size_grouping_over_time, 'yearly_sector_group-amount_group_heatmap_data.csv', 2023],
            '2024' : [plot_deal_size_grouping_over_time, 'yearly_sector_group-amount_group_heatmap_data.csv', 2024],
            '2025' : [plot_deal_size_grouping_over_time, 'yearly_sector_group-amount_group_heatmap_data.csv', 2025]
        },
    },
    'Funding Stages Analysis' : {
            'Deals Volume per Sector Groups by Funding Stages' : {
                'Default' : [dealsVolume_sectorGroup_fundingStages ,'deals_volume-sector_group_per_funding_stages.csv']
            },
            'Deal Size per Funding Stage over Time' : {
                'Average Deal Size (line)' : [dealSize_fundingStage_time, 'avg_deal_size-funding_stage-quarter.csv'],
                'Deal Volume' : [dealSize_fundingStage_time_bar, 'deals_volume-funding_stage-quarter.csv', 'Number of Deals'], 
                'Total Deal Size (bar)' : [dealSize_fundingStage_time_bar, 'deal_size-funding_stage-quarter_pivoted.csv', 'Deal Size']
            },
        },
    'Investor Demographics & Behavior' : {
            'Investment Count per Region' : {
                'Default' : [plot_dealsCount_investorRegion, 'investment_counts-region-round_type.csv']
            },
            'Investment Firms per Country by Funding Stages' : {
                'Default' : [plot_investor_count_country_funding_stage , 'investor_count-country-funding_stage.csv']
            },
            'Average Deal Size per Funding Stages by Region' : {
                'Default' : [plot_dealSize_investorRegion, 'avg-deal-size_investor-region_funding-stages.csv']
            },
            'Most Active Investment Firms over Time' : {
                'Default' : [plot_topFirms_quarter, 'top_firms-quarter.csv']
            },
        },
    'Sectoral & Regional Insights' : {
                'Top Sectors' : {
                    'Total' : [plot_top_sectors, 'amount_stats_by_tags.csv', 'Sum'],
                    'Mean' : [plot_top_sectors, 'amount_stats_by_tags.csv', 'Mean'],
                    'Count' : [plot_top_sectors, 'amount_stats_by_tags.csv', 'Count'],
                },
                'Top Sector Groups' : {
                    'Total' : [plot_top_sectors_group, 'amount_stats_by_sector_group.csv', 'Sum'],
                    'Mean' : [plot_top_sectors_group, 'amount_stats_by_sector_group.csv', 'Mean'],
                    'Count' : [plot_top_sectors_group, 'amount_stats_by_sector_group.csv', 'Count'],
                },
                'Top Regions' : {
                    'Total' : [plot_top_ecosystems, 'amount_stats_by_ecosystem.csv', 'Sum'],
                    'Mean' : [plot_top_ecosystems, 'amount_stats_by_ecosystem.csv', 'Mean'],
                    'Count' : [plot_top_ecosystems, 'amount_stats_by_ecosystem.csv', 'Count'],
                },
                'Investment by Ecosystem Over Time' : {
                    'Yearly' : [plot_investment_by_ecosystems_over_time, 'ecosystem-year_total_amount.csv', 'year'],
                    'Quarterly' : [plot_investment_by_ecosystems_over_time, 'ecosystem-quarter_total_amount.csv', 'yearQuarter']
                },
                'Treemap' : {
                    'Default' : [plot_tree_map, 'ecosystem-sector_group_investment.csv']
                },
                'Heatmap' : {
                    'Quarterly' : [plot_region_heatmap, 'quarter-ecosystem_amount_heatmap_data.csv']
                }
            },
        }