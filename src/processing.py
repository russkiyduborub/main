def filter_by_state(transactions, state = "EXECUTED"):
    new_transactions = []

    for transaction in transactions:
        if transaction["state"] == state:
            new_transactions.append(transaction)

    return new_transactions


def sort_by_date(transactions, reverse=True):
    pairs = []
    for transaction in transactions:
        date = transaction["date"]
        pairs.append(transaction["date"])

    pairs.sort(reverse=reverse)

    sorted_transactions = []
    for pair in pairs:
        sorted_transactions.append(pair)

    return sorted_transactions


transactions = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2023-02-09T11:14:47.175",
        "amount": 5000
    },
    {
        "id": 2,
        "state": "CANCELED",
        "date": "2024-07-01T01:32:33.921",
        "amount": 25000
    },
    {
        "id": 3,
        "state": "EXECUTED",
        "date": "2025-01-21T04:03:02.001",
        "amount": 1000
    }
]

executed = filter_by_state(transactions)
canceled = filter_by_state(transactions, "CANCELED")

sorted_by_date = sort_by_date(transactions, reverse=True)

print(filter_by_state(transactions))
print(sort_by_date(transactions, reverse=True))