import random


class Node(object):
    __slots__ = 'parent', 'label', 'children'

    def __init__(self, label, parent):
        self.parent = parent
        self.label = label
        self.children = []
        if parent:
            parent.children.append(self)

    def _print_children(self):
        return ', '.join(map(lambda x: str(x), self.children))

    def __repr__(self):
        ch = ': [' + self._print_children() + ']' if self.children else ''
        return str(self.label) + ch


def dfs(root):
    def visit(node):
        yield node
        for n in node.children:
            yield from visit(n)
    yield from visit(root)


def bfs(root):
    queue = [root]
    while queue:
        curr = queue.pop(0)
        yield curr
        for n in curr.children:
            queue.append(n)


def generate_tree(high):
    def check_level(node):
        level = 1
        while node.parent is not None:
            node = node.parent
            level += 1
        return level
    min = high
    max = 2**high - 1
    node_labels = random.randint(min, max)
    root = Node(1, None)
    tree = [root]
    for i in range(1, high):
        parent = tree[i-1]
        curr = Node(i+1, parent)
        tree.append(curr)
    tree.pop()
    for i in range(high, node_labels):
        parent = random.choice(tree)
        curr = Node(i+1, parent)
        if check_level(curr) != high:
            tree.append(curr)
    return root


if __name__ == "__main__":
    tree = generate_tree(5)
    print(tree)

#  %%
    print([i.label for i in bfs(tree)])
    print([i.label for i in dfs(tree)])
