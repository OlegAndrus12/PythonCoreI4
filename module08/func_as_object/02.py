def pipeline(*steps):
    def run(data):
        for step in steps:
            data = step(data)
        return data
    return run


def drop_nulls(records):
    return [r for r in records if r.get("amount") is not None]


def convert_to_usd(records):
    for r in records:
        r["amount"] = round(r["amount"] * 0.027, 2)
    return records


def flag_large_transactions(records):
    for r in records:
        r["large"] = r["amount"] > 100
    return records


process = pipeline(drop_nulls, convert_to_usd, flag_large_transactions)

transactions = [
    {"id": 1, "amount": 5000},
    {"id": 2, "amount": None},
    {"id": 3, "amount": 3000},
    {"id": 4, "amount": 12000},
]

for t in process(transactions):
    print(t)
