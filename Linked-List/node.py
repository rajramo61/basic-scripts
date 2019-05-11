class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

head = Node(2)
head.next = Node(1)

print(head.value)
print(head.next.value)

#================================

head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

print(head.next.next.value)
print(head.next.next.next.value)
print(head.next.next.next.next.value)