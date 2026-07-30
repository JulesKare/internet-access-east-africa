"""
Internet Access in Rwanda vs East Africa (SDG 9 / Digital Inclusion angle)
Author: Jules Karegeya Mugisha

This script loads the raw dataset, does basic cleaning/validation,
computes growth metrics, and produces three charts:
1. Rwanda's internet access trend over available years
2. Latest available cross-country comparison
3. Growth since earliest available year (Rwanda vs Kenya)
"""

import pandas as pd
import matplotlib.pyplot as plt

# ---- 1. Load & clean ----
df = pd.read_csv("../data/internet_access_east_africa.csv")

# Basic cleaning: strip whitespace, enforce types, check for missing/negative values
df["country"] = df["country"].str.strip()
df["year"] = df["year"].astype(int)
df["internet_users_pct_population"] = df["internet_users_pct_population"].astype(float)

assert df["internet_users_pct_population"].between(0, 100).all(), "Value out of valid percent range"
assert df.isnull().sum().sum() == 0, "Unexpected missing values"

print("Data loaded and validated:")
print(df)

# ---- 2. Chart 1: Rwanda trend ----
rwanda = df[df["country"] == "Rwanda"].sort_values("year")

plt.figure(figsize=(7, 4.5))
plt.plot(rwanda["year"], rwanda["internet_users_pct_population"], marker="o", linewidth=2, color="#1F3864")
for x, y in zip(rwanda["year"], rwanda["internet_users_pct_population"]):
    plt.annotate(f"{y:.1f}%", (x, y), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=9)
plt.title("Rwanda: Individuals Using the Internet (% of population)")
plt.xlabel("Year")
plt.ylabel("% of population")
plt.ylim(0, 45)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("../charts/01_rwanda_trend.png", dpi=150)
plt.close()

# ---- 3. Chart 2: latest available cross-country comparison ----
latest = df.sort_values("year").groupby("country").tail(1).sort_values("internet_users_pct_population")

colors = ["#8C1D18" if c == "Sub-Saharan Africa" else ("#1F3864" if c == "Rwanda" else "#7F9CC4") for c in latest["country"]]

plt.figure(figsize=(8, 5))
bars = plt.barh(latest["country"], latest["internet_users_pct_population"], color=colors)
for bar, (_, row) in zip(bars, latest.iterrows()):
    plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
              f"{row['internet_users_pct_population']:.1f}% ({row['year']})",
              va="center", fontsize=9)
plt.title("Internet Access: Rwanda vs East African Neighbors\n(latest year with published data per country)")
plt.xlabel("% of population using the internet")
plt.xlim(0, 42)
plt.tight_layout()
plt.savefig("../charts/02_latest_comparison.png", dpi=150)
plt.close()

# ---- 4. Chart 3: growth since earliest available year (Rwanda vs Kenya) ----
growth_rows = []
for country in ["Rwanda", "Kenya"]:
    sub = df[df["country"] == country].sort_values("year")
    first, last = sub.iloc[0], sub.iloc[-1]
    growth_rows.append({
        "country": country,
        "start_year": first["year"], "start_value": first["internet_users_pct_population"],
        "end_year": last["year"], "end_value": last["internet_users_pct_population"],
        "growth_pp": last["internet_users_pct_population"] - first["internet_users_pct_population"],
    })
growth_df = pd.DataFrame(growth_rows)
print("\nGrowth since earliest available year:")
print(growth_df)

plt.figure(figsize=(6, 4.5))
x = range(len(growth_df))
plt.bar(x, growth_df["growth_pp"], color=["#1F3864", "#7F9CC4"])
plt.xticks(x, [f"{r.country}\n({r.start_year}\u2192{r.end_year})" for r in growth_df.itertuples()])
for i, v in enumerate(growth_df["growth_pp"]):
    plt.text(i, v + 0.3, f"+{v:.1f} pp", ha="center", fontsize=10)
plt.title("Growth in Internet Access Since Earliest Available Year")
plt.ylabel("Percentage-point increase")
plt.tight_layout()
plt.savefig("../charts/03_growth_comparison.png", dpi=150)
plt.close()

print("\nCharts saved to ../charts/")
