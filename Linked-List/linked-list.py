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
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return
    
    def to_list(self):
        
        # TODO: Write function to turn Linked List into Python List
        if self.head is None:
            return []
        else:
            data = []
            node = self.head
            data.append(node.value)
            while node.next is not None:
                node = node.next
                data.append(node.value)
        return data


    def to_list_class(self):
        out_list = []

        node = self.head
        while node:
            out_list.append(node.value)
            node = node.next

        return out_list
 


# Test your method here
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(2)
linked_list.append(-1)
linked_list.append(0.2)

print ("Pass" if  (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")