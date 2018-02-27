def greedy_solution(knapsack):
    items = knapsack.sorted_items(knapsack.all_items)
    for item in items:
        knapsack.add_item(item)