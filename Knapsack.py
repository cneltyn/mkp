from copy import deepcopy
from pprint import pprint
from Item import Item
from time import clock

max_ind = 0

class Knapsack(object):

    def __init__(self, all_items, *args):
        self.value = 0
        self.all_items = all_items
        self.initial_value = 0
        self.items = []
        for ind, arg in enumerate(args):
            setattr(self, 'con{}'.format(ind+1), int(arg))
        global max_ind
        max_ind = len(args)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def optimization(self, initial_solution_function, heuristic_function=None, neighborhood_function=None):
        start = clock()
        initial_solution_function(self)
        self.initial_solution = deepcopy(self.items)
        self.initial_value = self.value
        end = clock()
        print ('Initial solution contains next items: ')
        for i in range(len(self.items)):
            print (vars(self.initial_solution[i]))
        print ('Initial value: %d' % self.initial_value)
        print ('Final value: %d' % self.value)
        #print ('Total improvement: %d' % (self.value - self.initial_value))
        for i in range(max_ind):
            print ('Con{} left: %d'.format(i+1) % getattr(self, 'con{}'.format(i+1)))
        print ('Number of items in solution: %s' % len(self.items))
        print ('Ran in %f milliseconds.' % ((end - start) * 1000))

    def add_item(self, item):
        if self.can_add_item(item):
            self.items.append(item)
            for i in range(max_ind):
                setattr(self, 'con{}'.format(i+1), getattr(self, 'con{}'.format(i+1)) - getattr(item, 'con{}'.format(i+1)))
            self.value += item.value
            self.all_items.remove(item)
            return True
        return False

    def sorted_items(self, items, key=Item.ratio):
        return sorted(items, key=key, reverse=True)

    def can_add_item(self, item):
        flag = not item in self.items
        for i in range(max_ind):
            flag = flag and getattr(self, 'con{}'.format(i+1)) >= getattr(item, 'con{}'.format(i+1))
        return flag
