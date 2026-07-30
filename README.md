# Internet Access in Rwanda vs East Africa

A small, self-directed data analysis project applying foundational data science skills
(data collection, cleaning, analysis, and visualization) to a real digital-development
question, in the spirit of UNDP's work on digital inclusion and the Sustainable
Development Goals (SDG 9: Industry, Innovation and Infrastructure).

## The question

How does Rwanda's internet access compare to its East African neighbors (Kenya, Uganda,
Tanzania, Burundi) and the Sub-Saharan Africa regional average - and how much progress
has Rwanda made over time?

## Data source

All figures are drawn from the **World Bank World Development Indicators**, indicator
`IT.NET.USER.ZS` - "Individuals using the Internet (% of population)" - accessed via
World Bank data and secondary aggregators in July 2026. Each row in
[`data/internet_access_east_africa.csv`](data/internet_access_east_africa.csv) is
labeled with its exact year and source, since not every country has a published figure
for every year (a common real-world constraint when working with international
development data).

**Note on data limitations:** country-level statistics for smaller economies (e.g.
Burundi) are sometimes revised between publication vintages, and coverage years differ
by country. This project uses the most recently published figures available at the time
of writing. For a fully rigorous or updated version, the complete indicator series can
be downloaded directly from the [World Bank Data Bank](https://data.worldbank.org/indicator/IT.NET.USER.ZS).

## Method

1. **Clean**: loaded the raw CSV, validated types and value ranges (percentages between
   0–100), checked for missing values.
2. **Analyze**: computed percentage-point growth for Rwanda and Kenya between their
   earliest and latest available data points.
3. **Visualize**: built three charts (see `charts/`) using pandas and matplotlib.

Run it yourself:
```bash
cd analysis
python3 analyze.py
```

## Findings

- **Rwanda's internet access grew from 18.0% (2015) to 34.2% (2023)** - a 16.2
  percentage-point increase over eight years.
- **Kenya grew faster in absolute terms** over a similar window (16.6% in 2015 to 35.0%
  in 2023, +18.4 percentage points), and both countries now sit close together, well
  above Uganda (15.3%, 2023) and Burundi (8.6%, 2024).
- **Rwanda and Kenya are both close to the Sub-Saharan Africa regional average (33.6%,
  2024)**, while Uganda and Burundi remain well below it - highlighting where regional
  digital-inclusion gaps are largest.

## Why this matters for digital development work

Internet access is a foundational enabler for nearly everything UNDP's Digital, AI and
Innovation Hub works on - digital public infrastructure, e-government services, and
inclusive digital transformation all depend on people actually being able to get online.
A simple comparison like this is a first step toward the kind of monitoring and
reporting work that tracks whether digital strategies are actually closing regional
gaps, not just improving national averages.

## Files

- `data/internet_access_east_africa.csv` - raw, sourced dataset
- `analysis/analyze.py` - cleaning, analysis, and chart-generation script
- `charts/01_rwanda_trend.png` - Rwanda's internet access over time
- `charts/02_latest_comparison.png` - latest available figures across countries
- `charts/03_growth_comparison.png` - growth since earliest available year, Rwanda vs Kenya

---
*Built by Jules Karegeya Mugisha as an independent data analysis exercise.*
