from copy import deepcopy
from Item import Item
from time import clock
from functools import reduce


max_ind = 0

class Knapsack(object):

    def __init__(self, all_items, *args, **kwargs):
        self.value = 0
        self.all_items = all_items
        self.initial_value = 0
        self.items = []
        self.movement_counter = 0
        self.moves_made = []
        for ind, arg in enumerate(args):
            setattr(self, 'con{}'.format(ind+1), int(arg))
        global max_ind
        max_ind = len(args)
        for key in kwargs.keys():
            setattr(self, key, kwargs[key])

    def optimization_tabu(self, initial_solution_function, heuristic_function=None, neighborhood_function=None):
        start = clock()
        initial_solution_function(self)
        self.initial_solution = deepcopy(self.items)
        self.initial_value = self.value
        heuristic_function(neighborhood_function, self)
        end = clock()
        print ('Initial solution contains next items: ')
        for i in range(len(self.items)):
            print (vars(self.initial_solution[i]))
        print ('Initial value: %d' % self.initial_value)
        print ('Final value: %d' % self.value)
        print ('Total improvement: %d' % (self.value - self.initial_value))
        for i in range(max_ind):
            print ('Con{} left: %d'.format(i+1) % getattr(self, 'con{}'.format(i+1)))
        print ('Number of items in solution: %s' % len(self.items))
        print ('Ran in %f milliseconds.' % ((end - start) * 1000))

    def optimization_local(self, initial_solution_function, heuristic_function=None, neighborhood_function=None):
        start = clock()
        initial_solution_function(self)
        self.initial_solution = deepcopy(self.items)
        self.initial_value = self.value
        heuristic_function(self)
        end = clock()
        print ('Initial solution contains next items: ')
        for i in range(len(self.items)):
            print (vars(self.initial_solution[i]))
        print ('Initial value: %d' % self.initial_value)
        print ('Final value: %d' % self.value)
        print ('Total improvement: %d' % (self.value - self.initial_value))
        for i in range(max_ind):
            print ('Con{} left: %d'.format(i+1) % getattr(self, 'con{}'.format(i+1)))
        print ('Number of items in solution: %s' % len(self.items))
        print ('Ran in %f milliseconds.' % ((end - start) * 1000))

    def execute_movement(self, movement, silent=False):
        for item in movement.remove_items:
            if not item in self:
                return False
            self.remove_item(item)
        for item in movement.add_items:
            if not self.can_add_item(item):
                return False
            self.add_item(item)
        if not silent:
            self.movement_counter += 1
            self.moves_made.append(movement)


    def add_item(self, item):
        if self.can_add_item(item):
            self.items.append(item)
            for i in range(max_ind):
                setattr(self, 'con{}'.format(i+1), getattr(self, 'con{}'.format(i+1)) - getattr(item, 'con{}'.format(i+1)))
            self.value += item.value
            self.all_items.remove(item)
            return True
        return False

    def evaluate_swap(self, item, another_item):
        return self.can_swap(item, another_item)

    def remove_item(self, item):
        if item in self.items:
            for i in range(max_ind):
                setattr(self, 'con{}'.format(i+1), getattr(self, 'con{}'.format(i+1)) + getattr(item, 'con{}'.format(i+1)))
            self.value -= item.value
            self.items.remove(item)
            self.all_items.append(item)
            return True
        return False

    def can_swap(self, inside_item, another_item):
        if inside_item not in self.items or another_item in self.items:
            return False
        if max_ind == 5:
            if (getattr(another_item, 'con{}'.format(1)) <= (getattr(self, 'con{}'.format(1))+getattr(inside_item, 'con{}'.format(1))) and
                    getattr(another_item, 'con{}'.format(2)) <= (getattr(self, 'con{}'.format(2))+getattr(inside_item, 'con{}'.format(2))) and
                    getattr(another_item, 'con{}'.format(3)) <= (getattr(self, 'con{}'.format(3))+getattr(inside_item, 'con{}'.format(3))) and
                    getattr(another_item, 'con{}'.format(4)) <= (getattr(self, 'con{}'.format(4))+getattr(inside_item, 'con{}'.format(4))) and
                    getattr(another_item, 'con{}'.format(5)) <= (getattr(self, 'con{}'.format(5))+getattr(inside_item, 'con{}'.format(5)))):
                return self.value - inside_item.value + another_item.value

        if max_ind == 10:
            if (getattr(another_item, 'con{}'.format(1)) <= (getattr(self, 'con{}'.format(1))+getattr(inside_item, 'con{}'.format(1))) and
                    getattr(another_item, 'con{}'.format(2)) <= (getattr(self, 'con{}'.format(2))+getattr(inside_item, 'con{}'.format(2))) and
                    getattr(another_item, 'con{}'.format(3)) <= (getattr(self, 'con{}'.format(3))+getattr(inside_item, 'con{}'.format(3))) and
                    getattr(another_item, 'con{}'.format(4)) <= (getattr(self, 'con{}'.format(4))+getattr(inside_item, 'con{}'.format(4))) and
                    getattr(another_item, 'con{}'.format(5)) <= (getattr(self, 'con{}'.format(5))+getattr(inside_item, 'con{}'.format(5))) and
                    getattr(another_item, 'con{}'.format(6)) <= (getattr(self, 'con{}'.format(6))+getattr(inside_item, 'con{}'.format(6))) and
                    getattr(another_item, 'con{}'.format(7)) <= (getattr(self, 'con{}'.format(7))+getattr(inside_item, 'con{}'.format(7))) and
                    getattr(another_item, 'con{}'.format(8)) <= (getattr(self, 'con{}'.format(8))+getattr(inside_item, 'con{}'.format(8))) and
                    getattr(another_item, 'con{}'.format(9)) <= (getattr(self, 'con{}'.format(9))+getattr(inside_item, 'con{}'.format(9))) and
                    getattr(another_item, 'con{}'.format(10)) <= (getattr(self, 'con{}'.format(10))+getattr(inside_item, 'con{}'.format(10)))):
                return self.value - inside_item.value + another_item.value

        if max_ind == 30:
            if (getattr(another_item, 'con{}'.format(1)) <= (getattr(self, 'con{}'.format(1))+getattr(inside_item, 'con{}'.format(1))) and
                    getattr(another_item, 'con{}'.format(2)) <= (getattr(self, 'con{}'.format(2))+getattr(inside_item, 'con{}'.format(2))) and
                    getattr(another_item, 'con{}'.format(3)) <= (getattr(self, 'con{}'.format(3))+getattr(inside_item, 'con{}'.format(3))) and
                    getattr(another_item, 'con{}'.format(4)) <= (getattr(self, 'con{}'.format(4))+getattr(inside_item, 'con{}'.format(4))) and
                    getattr(another_item, 'con{}'.format(5)) <= (getattr(self, 'con{}'.format(5))+getattr(inside_item, 'con{}'.format(5))) and
                    getattr(another_item, 'con{}'.format(6)) <= (getattr(self, 'con{}'.format(6))+getattr(inside_item, 'con{}'.format(6))) and
                    getattr(another_item, 'con{}'.format(7)) <= (getattr(self, 'con{}'.format(7))+getattr(inside_item, 'con{}'.format(7))) and
                    getattr(another_item, 'con{}'.format(8)) <= (getattr(self, 'con{}'.format(8))+getattr(inside_item, 'con{}'.format(8))) and
                    getattr(another_item, 'con{}'.format(9)) <= (getattr(self, 'con{}'.format(9))+getattr(inside_item, 'con{}'.format(9))) and
                    getattr(another_item, 'con{}'.format(10)) <= (getattr(self, 'con{}'.format(10))+getattr(inside_item, 'con{}'.format(10))) and
                    getattr(another_item, 'con{}'.format(11)) <= (getattr(self, 'con{}'.format(11))+getattr(inside_item, 'con{}'.format(11))) and
                    getattr(another_item, 'con{}'.format(12)) <= (getattr(self, 'con{}'.format(12))+getattr(inside_item, 'con{}'.format(12))) and
                    getattr(another_item, 'con{}'.format(13)) <= (getattr(self, 'con{}'.format(13))+getattr(inside_item, 'con{}'.format(13))) and
                    getattr(another_item, 'con{}'.format(14)) <= (getattr(self, 'con{}'.format(14))+getattr(inside_item, 'con{}'.format(14))) and
                    getattr(another_item, 'con{}'.format(15)) <= (getattr(self, 'con{}'.format(15))+getattr(inside_item, 'con{}'.format(15))) and
                    getattr(another_item, 'con{}'.format(16)) <= (getattr(self, 'con{}'.format(16))+getattr(inside_item, 'con{}'.format(16))) and
                    getattr(another_item, 'con{}'.format(17)) <= (getattr(self, 'con{}'.format(17))+getattr(inside_item, 'con{}'.format(17))) and
                    getattr(another_item, 'con{}'.format(18)) <= (getattr(self, 'con{}'.format(18))+getattr(inside_item, 'con{}'.format(18))) and
                    getattr(another_item, 'con{}'.format(19)) <= (getattr(self, 'con{}'.format(19))+getattr(inside_item, 'con{}'.format(19))) and
                    getattr(another_item, 'con{}'.format(20)) <= (getattr(self, 'con{}'.format(20))+getattr(inside_item, 'con{}'.format(20))) and
                    getattr(another_item, 'con{}'.format(21)) <= (getattr(self, 'con{}'.format(21))+getattr(inside_item, 'con{}'.format(21))) and
                    getattr(another_item, 'con{}'.format(22)) <= (getattr(self, 'con{}'.format(22))+getattr(inside_item, 'con{}'.format(22))) and
                    getattr(another_item, 'con{}'.format(23)) <= (getattr(self, 'con{}'.format(23))+getattr(inside_item, 'con{}'.format(23))) and
                    getattr(another_item, 'con{}'.format(24)) <= (getattr(self, 'con{}'.format(24))+getattr(inside_item, 'con{}'.format(24))) and
                    getattr(another_item, 'con{}'.format(25)) <= (getattr(self, 'con{}'.format(25))+getattr(inside_item, 'con{}'.format(25))) and
                    getattr(another_item, 'con{}'.format(26)) <= (getattr(self, 'con{}'.format(26))+getattr(inside_item, 'con{}'.format(26))) and
                    getattr(another_item, 'con{}'.format(27)) <= (getattr(self, 'con{}'.format(27))+getattr(inside_item, 'con{}'.format(27))) and
                    getattr(another_item, 'con{}'.format(28)) <= (getattr(self, 'con{}'.format(28))+getattr(inside_item, 'con{}'.format(28))) and
                    getattr(another_item, 'con{}'.format(29)) <= (getattr(self, 'con{}'.format(29))+getattr(inside_item, 'con{}'.format(29))) and
                    getattr(another_item, 'con{}'.format(30)) <= (getattr(self, 'con{}'.format(30))+getattr(inside_item, 'con{}'.format(30)))):
                return self.value - inside_item.value + another_item.value

        return False

    def swap(self, item, another_item):
        if self.can_swap(item, another_item):
            self.remove_item(item)
            self.add_item(another_item)
            return True
        return False

    def __contains__(self, item):
        return any(map(lambda x: x == item, self.items))

    def sorted_items(self, items, key=Item.ratio):
        return sorted(items, key=key, reverse=True)

    def __repr__(self):
        return "<Knapsack (%d) %s" % (len(self.items), repr(self.items))

    def can_add_item(self, item):
        flag = not item in self.items
        for i in range(max_ind):
            flag = flag and getattr(self, 'con{}'.format(i+1)) >= getattr(item, 'con{}'.format(i+1))
        return flag

class Movement(object):

    def __init__(self, add_items=[], remove_items=[]):
        self.add_items = add_items
        self.remove_items = remove_items

    @property
    def movement_avaliation(self):
        remove_value = add_value = 0
        if not len(self.remove_items) == 0:
            remove_value = reduce(lambda x, y: x + y, [item.value for item in self.remove_items])
        if not len(self.add_items) == 0:
            add_value = reduce(lambda x, y: x + y, [item.value for item in self.add_items])
        return add_value - remove_value

    def reverse(self):
        return Movement(add_items=self.remove_items, remove_items=self.add_items)

    def __eq__(self, another_move):
        if not isinstance(another_move, Movement):
            return False
        return self.add_items == another_move.add_items and self.remove_items == another_move.remove_items




