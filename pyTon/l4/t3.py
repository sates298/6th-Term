class Node(object):
    __slots__ = 'parent', 'label', 'children', 'met'

    def __init__(self, label, parent):
        self.parent = parent
        self.label = label
        self.children = None, None
        self.met = False
