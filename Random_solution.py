from copy import deepcopy
from random import shuffle

def random_solution(knapsack):
    items = deepcopy(knapsack.all_items)
    shuffle(items)
    for item in items:
        if knapsack.can_add_item(item):
            knapsack.add_item(item)
        else:
            continue