import random
# ["1", ["2", ["4",["8", None, None], ["9",None,None]], ["5",None,None]],\\
# ["3", ["6", None, None], ["7", None, None]]]


def generate_tree(high):
    def build_node(root):
        return [str(root), None, None]

    def get_lowest_in_line(current):
        if not current[1] and not current[2]:
            return current
        else:
            if not current[1]:
                return get_lowest_in_line(current[2])
            else:
                return get_lowest_in_line(current[1])

    nodes_no = random.randint(high, 2**high - 1)
    root = build_node(1)
    levels = {'1': 1}
    curr = root
    for i in range(1, high):
        curr = get_lowest_in_line(curr)
        rdm = random.random()
        if rdm < 0.5:
            curr[1] = build_node(i+1)
        else:
            curr[2] = build_node(i+1)
        levels[f'{i+1}'] = i+1

    for i in range(high, nodes_no):
        new = build_node(i+1)
        inserted = False
        curr = root
        while not inserted:
            if levels[curr[0]] == high:
                curr = root
            rdm = random.random()
            if not curr[1] and not curr[2]:
                if rdm < 0.5:
                    curr[1] = new
                    inserted = True
                    levels[f'{i+1}'] = levels[curr[0]] + 1
                else:
                    curr[2] = new
                    inserted = True
                    levels[f'{i+1}'] = levels[curr[0]] + 1
            elif not curr[1]:
                if rdm < 0.5:
                    curr[1] = new
                    inserted = True
                    levels[f'{i+1}'] = levels[curr[0]] + 1
                else:
                    curr = curr[2]
            elif not curr[2]:
                if rdm < 0.5:
                    curr[2] = new
                    inserted = True
                    levels[f'{i+1}'] = levels[curr[0]] + 1
                else:
                    curr = curr[1]
            else:
                if rdm < 0.5:
                    curr = curr[1]
                else:
                    curr = curr[2]

    return root


def bfs(root):
    queue = []
    if root:
        queue.append(root)
    while queue:
        curr = queue.pop(0)
        yield curr[0]
        for n in curr[1:]:
            if n:
                queue.append(n)


def dfs(root):
    def visit(node):
        if node:
            yield node[0]
            for n in node[1:]:
                yield from visit(n)
    yield from visit(root)


if __name__ == '__main__':
    tree = generate_tree(3)
    print(tree)

# %%
    print(list(bfs(tree)))
    print(list(dfs(tree)))
