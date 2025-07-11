# ╭────────────────────────────────╮
# │   HeatMap Config               |
# ╰────────────────────────────────╯

heatmap_config = {
    "aggregations": {
        "ORISPL": "count",
        "Total Nameplate Capacity (MW)": "sum",
        "Retiring Capacity": "sum",
        "Summed Generator annual net generation (MWh)": "median",
        "Average Capacity Factor": "mean",
        "Generator Size Weighted Age": "mean",
        "2022 CO2 Emission Rate (lb/mmBtu)": "mean",
        "2022 SO2 Emission Rate (lb/mmBtu)": "mean",
        "PM 2.5 Emission Rate (lb/MWh)": "mean",
        "$ Asthma Exacerbation": "mean",
        "total population (ACS2018)": "median",
        "National percentile for Low Income Population": "mean",
        "Total Cost of Emissions Control Equiptment Retrofits Installed since 2012 ($)": "sum",
        "Forward Costs": "mean",
        "Difference between cheapest renewables and coal ($/MWh)": "mean",
        "Estimated percentage who somewhat/strongly oppose setting strict limits on existing coal-fire power plants": "mean",
        "Change from 2018 to 2021 in trhe estimated percentage who somewhat/strongly oppose setting strict limits on existing coal-fire power plants": "median",
    },
    "renaming": {
        "ORISPL": "Plant Count",
        "Generator Size Weighted Age": "Average Plant Age",
        "$ Asthma Exacerbation": "Average Asthma Exacerbation Costs ($)",
        "2022 CO2 Emission Rate (lb/mmBtu)": "CO2 Rate (lb/mmBtu)",
        "2022 SO2 Emission Rate (lb/mmBtu)": "SO2 Rate (lb/mmBtu)",
        "PM 2.5 Emission Rate (lb/MWh)": "PM2.5 Rate (lb/MWh)",
        "total population (ACS2018)": "Average Population within 3 Miles (ACS2018)",
        "National percentile for Low Income Population": "Low Income Percentile",
        "Forward Costs": "Median MCOE ($/MWh)",
        "Difference between cheapest renewables and coal ($/MWh)": "Renewables LCOE Advantage over Coal ($/MWh)",
        "Estimated percentage who somewhat/strongly oppose setting strict limits on existing coal-fire power plants": "Average County-level Support for Coal (%)",
        "Change from 2018 to 2021 in trhe estimated percentage who somewhat/strongly oppose setting strict limits on existing coal-fire power plants": "Growing Support for Coal (% increase 2018–2021)",
    },
    "derived_columns": [
        {
            "name": "Group Retiring Capacity (GW)",
            "formula": lambda df: df["Retiring Capacity"] / 1000,
            "input": "group",
        },
        {
            "name": "Group Nameplate (GW)",
            "formula": lambda df: df["Total Nameplate Capacity (MW)"] / 1000,
            "input": "group",
        },
        {
            "name": "Emissions Control Retrofits Cost ($/MW)",
            "formula": lambda df: (
                df[
                    "Total Cost of Emissions Control Equiptment Retrofits Installed since 2012 ($)"
                ]
                / df["Total Nameplate Capacity (MW)"]
            ),
            "input": "group",
        },
        {
            "name": "Average Generation (GWh/yr)",
            "formula": lambda df: df["Summed Generator annual net generation (MWh)"]
            / 1000,
            "input": "group",
        },
        {
            "name": "Average Capacity Factor (%)",
            "formula": lambda df: df["Average Capacity Factor"] * 100,
            "input": "group",
        },
        {
            "name": "In State w/ Republican Legislature (% of Plants)",
            "formula": lambda df: (
                (
                    df[df["Legislation Majority Party"] == "Republican"]
                    .groupby("Group")
                    .size()
                    / df.groupby("Group").size()
                ).fillna(0)
                * 100
            ),
            "input": "raw",
        },
    ],
    "categories": {
        "Operational": [
            "Plant Count",
            "Group Nameplate (GW)",
            "Group Retiring Capacity (GW)",
            "Average Generation (GWh/yr)",
            "Average Capacity Factor (%)",
            "Average Plant Age",
        ],
        "Environmental": [
            "CO2 Rate (lb/mmBtu)",
            "SO2 Rate (lb/mmBtu)",
            "PM2.5 Rate (lb/MWh)",
            "Average Asthma Exacerbation Costs ($)",
        ],
        "Social Impact": [
            "Average Population within 3 Miles (ACS2018)",
            "Low Income Percentile",
        ],
        "Economic": [
            "Emissions Control Retrofits Cost ($/MW)",
            "Median MCOE ($/MWh)",
            "Renewables LCOE Advantage over Coal ($/MWh)",
        ],
        "Political": [
            "Average County-level Support for Coal (%)",
            "Growing Support for Coal (% increase 2018–2021)",
            "In State w/ Republican Legislature (% of Plants)",
        ],
    },
}
