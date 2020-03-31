import random
# ["1", ["2", ["4",["8", None, None], ["9",None,None]], ["5",None,None]],["3", ["6", None, None], ["7", None, None]]]


def build_tree(high):
    nodes_no = random.randint(2**(high-1), 2**high - 1)
    nodes = list(range(1, nodes_no+1))
    curr = 1

    def build_level(root, left, right):
        return [str(root), left, right]

    def build_subtree(current):
        pass


def main():
    build_tree(3)


if __name__ == '__main__':
    main()
