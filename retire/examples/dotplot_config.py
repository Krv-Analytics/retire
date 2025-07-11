# ╭────────────────────────────────╮
# │   HeatMap Config               |
# ╰────────────────────────────────╯
import pandas as pd

dotplot_config = {
    "features": [
        "Total Nameplate Capacity (MW)",
        "Summed Generator annual net generation (MWh)",
        "Average Capacity Factor",
        "Age",
        "2022 NOX Emission Rate (lb/mmBtu)",
        "2022 Hg Emission Rate (lb/TBtu)",
        "2022 Hg Emissions (lbs)",
        "total population (ACS2018)",
        "$ Asthma Exacerbation",
        "Total Cost of Emissions Control Equiptment Retrofits Installed since 2012 ($)",
        "OH_Legislation Majority Party_Republican",
        "Estimated percentage who somewhat/strongly oppose setting strict limits on existing coal-fire power plants",
        "National percentile for Demographic Index",
        "2020 Net Cashflow",
        "Forward Costs",
        "eGRID subregion wind generation percent (resource mix)",
    ],
    "feature_labels": {
        "eGRID subregion wind generation percent (resource mix)": "eGRID Subregion Wind Generation (% of Resource Mix)",
        "OH_Legislation Majority Party_Republican": "Legislation Majority Party (Red: Republican, Blue: Democrat)",
        "total population (ACS2018)": "Total Population within 3 Miles",
        "$ Asthma Exacerbation": "Asthma Exacerbation ($)",
        "Total Nameplate Capacity (MW)": "Nameplate Coal Capacity (MW)",
        "Summed Generator annual net generation (MWh)": "Annual Coal Generation (MWh)",
        "Age": "Plant Age",
        "Estimated percentage who somewhat/strongly oppose setting strict limits on existing coal-fire power plants": "Public Opinion in Favor of Coal Power",  # optional for clarity
    },
    "normalize_feature": lambda s: (
        pd.Series(0.5, index=s.index)
        if s.min() == s.max()
        else (s - s.min()) / (s.max() - s.min())
    ),
    "normalize": "per_feature",
    "color_map": "coolwarm",
    "dot_size_range": (10, 650),
}
