countries = ["Germany", "France", "Poland", "Japan", "USA", "Brazil"]
codes = ["DE", "FR", "PL", "JP", "US", "BR"]

for country, code in zip(countries, codes):
    print(f"  {code} — {country}")
