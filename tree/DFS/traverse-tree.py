from tree.DFS.tree import Tree


class TraverseTree(Tree):
    @staticmethod
    def pre_order(tree):
        """
        Visit the node, then traverse left subtree, and then right subtree.
        :param tree:
        :return:
        """
        visited = list()
        node = tree.get_root()

        def traverse(node):
            if node:
                visited.append(node.get_value())
                traverse(node.get_left_child())
                traverse(node.get_right_child())

        traverse(node)
        return visited

    @staticmethod
    def in_order(tree):
        """
        Traverse left subtree, then visit the node, and then right subtree.
        :param tree:
        :return:
        """
        visited = list()
        node = tree.get_root()

        def traverse(node):
            if node:
                traverse(node.get_left_child())
                visited.append(node.get_value())
                traverse(node.get_right_child())

        traverse(node)
        return visited

    @staticmethod
    def post_order(tree):
        """
        Traverse left subtree, then right subtree, and then visit the node.
        :param tree:
        :return:
        """
        visited = list()
        node = tree.get_root()

        def traverse(node):
            if node:
                traverse(node.get_left_child())
                traverse(node.get_right_child())
                visited.append(node.get_value())

        traverse(node)
        return visited

        pass
