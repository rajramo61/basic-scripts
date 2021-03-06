"""
Least Recently Used Cache
We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit.
If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache.
If the cache is full and we want to add a new entry to the cache, we use some criteria to
remove an element. After removing an element, we use the put() operation to insert the new element.
The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used
(LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when
 the cache memory reaches its limit.

Your job is to use appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element.
If the cache is full, you must write code that removes the least recently used entry first and
then insert the element. All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.
"""


class DLL(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.head = DLL()
        self.tail = DLL()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.table = {}
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.table:
            value = self.table.get(key).value
            node = self.table.get(key)
            if node is self.head.next:
                return value
            else:
                # Remove node
                node.prev.next = node.next
                node.next.prev = node.prev
                # Add node at the front
                node.next = self.head.next
                node.prev = self.head
                self.head.next.prev = node
                self.head.next = node
            return value
        else:
            return -1
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key:
            if key in self.table:
                self.table[key].value = value
                node = self.table[key]
                if node is self.head.next:
                    return
                else:
                    # Remove node
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    # Add node at the front
                    node.next = self.head.next
                    node.prev = self.head
                    self.head.next.prev = node
                    self.head.next = node
            else:
                if self.capacity == len(self.table):
                    del_node = self.tail.prev
                    del self.table[del_node.key]
                    del_node.prev.next = self.tail
                    self.tail.prev = del_node.prev

                # Create new node
                new_node = DLL(key, value)
                # Add node to the table
                self.table[key] = new_node
                new_node.next = self.head.next
                new_node.prev = self.head
                self.head.next.prev = new_node
                self.head.next = new_node
        pass


our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.get(1))  # returns -1
print(our_cache.get(2))  # returns 2
print(our_cache.get(3))  # return 3
print(our_cache.get(9))  # return -1
our_cache.set(9, 9)
print(our_cache.get(9))  # return 9

our_cache2 = LRU_Cache(2)
our_cache2.set(1, 1)
our_cache2.set(2, 2)
print(our_cache2.get(1))    # return 1
our_cache2.set(3, 3)
print(our_cache2.get(2))    # return -1

our_cache3 = LRU_Cache(3)
our_cache3.set(1, 1)
our_cache3.set(2, 2)
our_cache3.set(3, 3)
our_cache3.set(4, 4)
print(our_cache3.get(4))    # return 4
print(our_cache3.get(3))    # return 3
print(our_cache3.get(2))    # return 2
print(our_cache3.get(1))    # return -1
our_cache3.set(5, 5)
print(our_cache3.get(1))    # return -1
print(our_cache3.get(2))    # return 2
print(our_cache3.get(3))    # return 3
print(our_cache3.get(4))    # return -1
print(our_cache3.get(5))    # return 5

our_cache4 = LRU_Cache(1)
our_cache4.set(2, 1)
print(our_cache4.get(2))    # return 1
our_cache4.set(3, 2)
print(our_cache4.get(3))    # return 2

our_cache5 = LRU_Cache(2)
our_cache5.set(2, 1)
our_cache5.set(1, 1)
our_cache5.set(2, 3)
our_cache5.set(4, 1)
print(our_cache5.get(1))    # return -1
print(our_cache5.get(2))    # return 3

our_cache6 = LRU_Cache(10)
our_cache6.set(7, 28)
our_cache6.set(7, 1)
our_cache6.set(8, 15)
print(our_cache6.get(6))    # return -1
our_cache6.set(10, 27)
our_cache6.set(8, 10)
print(our_cache6.get(8))    # return 10
our_cache6.set(6, 29)
our_cache6.set(1, 9)
print(our_cache6.get(6))    # return 29
our_cache6.set(10, 7)
print(our_cache6.get(1))    # return 9
print(our_cache6.get(2))    # return -1
print(our_cache6.get(13))    # return -1
our_cache6.set(8, 30)
our_cache6.set(1, 5)
print(our_cache6.get(1))    # return 5
our_cache6.set(13, 2)
our_cache6.set(1, 2)

"""
Data Structure:
    Read and write operations to do in constant time, we need HashMap. 
    In Python, we have dictionary for this purpose.
    To add entry at the beginning and deletion at the end to maintain the size of cache, 
    and to maintain the LRU for cache, we can use doubly linked list. 
    My solution uses the combination of both.

Time Complexity:
    get and set both methods use constant time to do the job. The time complexity is O(1)
    get - does a lookup using dictionary so the lookup time in O(1)
    set - does the insertion is constant time
Space Complexity: O(n)
    At maximum, we need n (max capacity) node in out dictionary to manage this cache.
"""
