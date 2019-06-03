from tree.BFS.queue import Queue


def bfs(tree):
    visit_order = list()
    q = Queue()
    root_node = tree.get_root()
    if root_node:
        q.enq(root_node)
        print(q)
        node = q.deq()
        while node:
            visit_order.append(node)
            if node.has_left_child():
                q.enq(node.get_left_child())
            if node.has_right_child():
                q.enq(node.get_right_child())
            node = q.deq()
    return visit_order
    pass


def bfs_learn(tree):
    visit_order = list()
    q = Queue()
    node = tree.get_root()
    q.enq(node)
    while len(q) > 0:
        node = q.deq()
        visit_order.append(node)
        if node.has_left_child():
            q.enq(node.get_left_child())
        if node.has_right_child():
            q.enq(node.get_right_child())
    return visit_order
    pass
