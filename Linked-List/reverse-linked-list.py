class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])


def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    
    # TODO: Write your function to reverse linked lists here
    if linked_list.head is None:
        return None
    new_llist = LinkedList()
    next_node = None
    current_node = linked_list.head
    while current_node:
        next_node = current_node.next
        current_node.next = new_llist.head
        new_llist.head = current_node
        current_node = next_node
    # if linked_list.head is None:
    #     return None
    # new_llist = LinkedList()
    # currenrt_node = linked_list.head
    # while currenrt_node:
    #     node = Node(currenrt_node.value)
    #     if new_llist.head is None:
    #         new_llist.head = node
    #     else:
    #         node.next = new_llist.head
    #         new_llist.head = node
    #     currenrt_node = currenrt_node.next
    # return new_llist
    # for val in linked_list:
    #     if new_llist.head is None:
    #         new_llist.head = Node(val)
    #     else:
    #         node = Node(val)
    #         node.next = new_llist.head
    #         new_llist.head = node
    # linked_list = new_llist
    # return linked_list
    return new_llist
    pass


def reverse_class(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    new_list = LinkedList()
    node = linked_list.head
    
    # A bit of a complex operation here. We want to take the
    # node from the original linked list and prepend it to 
    # the new linked list
    while node:
        old_head = new_list.head
        new_node = node
        node = node.next
        
        new_node.next = old_head
        new_list.head = new_node
    return new_list


llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

print(reverse(llist))
print ("Pass" if (llist == reverse(llist)) else "Fail")