import re

description = "Sale! Was $199.99, now only $89.00. Accessories from $4.99."

prices = re.findall(r"\$\d+\.\d{2}", description)
print("Prices found:", prices)
