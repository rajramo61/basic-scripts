def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    head = None
    current_node, tail_node = None, None
    for input in input_list:
        current_node = Node(input)
        if head == None:
            head = current_node
            tail_node = current_node
        else:
            tail_node.next = current_node
            tail_node = tail_node.next
    return head


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def traverse(head):
    current_node = head
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next


head1 = create_linked_list([1, 2, 3, 4, 5, 6])
traverse(head1)

### Test Code
# def test_function(input_list, head):
#     try:
#         if len(input_list) == 0:
#             if head is not None:
#                 print("Fail")
#                 return
#         for value in input_list:
#             if head.value != value:
#                 print("Fail")
#                 return
#             else:
#                 head = head.next
#         print("Pass")
#     except Exception as e:
#         print("Fail: "  + e)
        
        

# input_list = [1, 2, 3, 4, 5, 6]
# head = create_linked_list(input_list)
# test_function(input_list, head)

# input_list = [1]
# head = create_linked_list(input_list)
# test_function(input_list, head)

# input_list = []
# head = create_linked_list(input_list)
# test_function(input_list, head)