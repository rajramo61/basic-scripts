'''
Detecting Loops in Linked Lists¶
In this notebook, you'll implement a function that detects if a loop exists in a linked list. 
The way we'll do this is by having two pointers, called "runners", moving through the list at different 
rates. Typically we have a "slow" runner which moves at one node per step and a "fast" runner that moves
 at two nodes per step.

If a loop exists in the list, the fast runner will eventually move behind the slow runner as it moves to 
the beginning of the loop. Eventually it will catch up to the slow runner and both runners will be 
pointing to the same node at the same time. If this happens then you know there is a loop in the linked 
list. 
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return


list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next: 
    node = node.next   
node.next = loop_start


def is_circular(linked_list):
    """
    Determine wether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """
    
    # TODO: Write function to check if linked list is circular
    slow = fast = linked_list.head
    while slow is not None and fast is not None:
        if fast.next is None or slow.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
    pass


print("Pass" if (is_circular(list_with_loop) == True) else "Fail")
print("Pass" if (is_circular(LinkedList([1])) == False) else "Fail")
