from tree.BST.node import Node
from tree.BST.queue import Queue


class Tree:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1  # traverse left
        else:  # new_node > node
            return 1  # traverse right

    def insert_with_loop(self, new_value):
        new_node = Node(new_value)
        node = self.get_root()
        if node is None:
            self.root = new_node
            return

        while (True):
            comparison = self.compare(node, new_node)
            if comparison == 0:
                # override with new node's value
                node.set_value(new_node.get_value())
                break  # override node, and stop looping
            elif comparison == -1:
                # go left
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break  # inserted node, so stop looping
            else:  # comparison == 1
                # go right
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break  # inserted node, so stop looping

    def insert_with_recursion(self, value):

        if self.get_root() is None:
            self.set_root(value)
            return
        # otherwise, use recursion to insert the node
        self.insert_recursively(self.get_root(), Node(value))

    def insert_recursively(self, node, new_node):
        comparison = self.compare(node, new_node)
        if comparison == 0:
            # equal
            node.set_value(new_node.get_value())
        elif comparison == -1:
            # traverse left
            if node.has_left_child():
                self.insert_recursively(node.get_left_child(), new_node)
            else:
                node.set_left_child(new_node)

        else:  # comparison == 1
            # traverse right
            if node.has_right_child():
                self.insert_recursively(node.get_right_child(), new_node)
            else:
                node.set_right_child(new_node)

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while len(q) > 0:
            node, level = q.deq()
            if node is None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s

# https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
