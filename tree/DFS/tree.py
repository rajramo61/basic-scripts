from tree.DFS.node import Node


class Tree(object):
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

