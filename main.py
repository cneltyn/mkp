from Greedy_solution import greedy_solution
from Random_solution import random_solution

from Item import Item
from Knapsack import Knapsack

def items_from_file(filename):
    items = []
    weights = []
    lines = open(filename).readlines()
    lines = [line.strip().split(' ') for line in lines]
    numbers_of_items = int(lines[0][0])
    for i in range(numbers_of_items):
        for j in range(2, len(lines) - 1):
            weights.append(lines[j][i])
        item = Item('Item %d' % i, int(lines[1][i]), *weights)
        items.append(item)
        weights = []
    return items

def constraints_from_file(filename):
    lines = open(filename).readlines()
    return lines[-1].split()

def bag_from_file(filename):
    constraints = constraints_from_file(filename)
    return (items_from_file(filename), *constraints)

if __name__ == '__main__':
    bag = Knapsack(*bag_from_file('instances_shared/class5/250-10-03.txt'))
    bag.optimization(greedy_solution)
