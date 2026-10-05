# Travel expenses for multiple trips
travel_costs = [
    [500, 150, 100, 50],
    [200, 300, 120, 80],
    [180, 220, 130, 170],
    # … (rest omitted for brevity)
]

min_expense = 100
significant_threshold = 200

significant_expenses = []
i = 0
while i < len(travel_costs):
    first_significant = None
    for cost in travel_costs[i]:
        if cost < min_expense:
            continue
        if cost > significant_threshold:
            first_significant = cost
            break
    significant_expenses.append(first_significant)
    i += 1

print('First Significant Expenses:', significant_expenses)