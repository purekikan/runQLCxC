import dealsize_analysis
import dealsize_analysis_2
import funding_analysis
import investor_demographics
import q3_sub2
import q3_sub3
import q3_sub5

if __name__ == "__main__":
    funding_analysis.analyze_funding_stages()
    dealsize_analysis.analyze_deal_size_evolution()
    dealsize_analysis_2.analyze_deal_trends()
    investor_demographics.plot_investor_demographics()
    q3_sub2.analyze_investment_firms_by_country_and_stage()
    q3_sub3.analyze_avg_deal_size_by_stage_and_geography()
    q3_sub5.plot_investment_firm_activity()