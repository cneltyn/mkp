class Item(object):

    max_ind = 0

    def __init__(self, name, value, *args):
        self.name = name
        self.value = value
        for ind, arg in enumerate(args):
            setattr(self, 'con{}'.format(ind+1), int(arg))
        global max_ind
        max_ind = len(args)

    def ratio(self):
        sum = 0
        for i in range(max_ind):
            sum += getattr(self, 'con{}'.format(i+1))
        return self.value / sum

    def __eq__(self, item):
        flag = self.name == item.name and self.value == item.value
        for i in range(max_ind):
            flag = flag and getattr(self, 'con{}'.format(i+1)) == getattr(item, 'con{}'.format(i+1))
        return flag
