from Knapsack import Movement
from random import choice, shuffle
from copy import deepcopy
from Knapsack import max_ind

def first_improving_neighborhood(knapsack):
    neighborhood = []
    for item in knapsack.sorted_items(knapsack.all_items):
        actual_value = knapsack.value
        print ("Test", actual_value)
        for solution_item in knapsack.sorted_items(knapsack.items):
            if knapsack.can_swap(solution_item, item):
                new_value = knapsack.evaluate_swap(solution_item, item)
                movement = Movement(add_items=[item,], remove_items=[solution_item,])
                if new_value > knapsack.value:
                    neighborhood.append(movement)
                    print ('Test1', new_value)
                    return neighborhood
                neighborhood.append(movement)
            else:
                pass
    return neighborhood

def best_improving(knapsack):
    solutions = first_improving_neighborhood(knapsack)
    sorted_moves = sort_moves(solutions)
    best_solution = knapsack.value
    best_solution_moves = deepcopy(knapsack.moves_made)
    best_solution_items = deepcopy(knapsack.items)
    if not len(sorted_moves) == 0:
        candidate_move = sorted_moves.pop(0)
        actual_solution = knapsack.value + candidate_move.movement_avaliation
        knapsack.execute_movement(candidate_move)
        if actual_solution > best_solution:
            best_solution = actual_solution
            best_solution_moves = deepcopy(knapsack.moves_made)
            best_solution_items = deepcopy(knapsack.items)

    knapsack.value = best_solution
    knapsack.items = best_solution_items
    knapsack.moves_made = best_solution_moves

    return False


def sort_moves(moves):
       return sorted(moves, key=lambda x: x.movement_avaliation, reverse=True)