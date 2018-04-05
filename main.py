from Greedy_solution import greedy_solution
from Random_solution import random_solution
import Neighborhood
from Item import Item
from Knapsack import Knapsack
from TabuSearch import TabuList, TabuSearch

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
    bag = Knapsack(*bag_from_file('instances_shared/class1/100-5-01.txt'), tabu_list=TabuList(200))
    # local search heuristic
    bag.optimization_local(greedy_solution, Neighborhood.best_improving, Neighborhood.first_improving_neighborhood)
    # Tabu metaheuristic
    # bag.optimization_tabu(greedy_solution, TabuSearch(300), Neighborhood.first_improving_neighborhood)
    