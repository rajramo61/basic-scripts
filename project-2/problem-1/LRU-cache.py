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
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.table = {}
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.table:
            return self.table.get(key).value
        else:
            return -1
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key:
            if key in self.table:
                self.table[key].value = value
            else:
                if self.capacity == len(self.table):
                    del self.table[self.tail.key]
                    self.tail = self.tail.prev
                node = DLL(key, value)
                self.table[key] = node
                node.next = self.head
                self.head = node
                if self.tail is None:
                    self.tail = node
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

"""
Data Structure:
    Read and write operations to do in constant time, we need HashMap. 
    In Python, we have dictionary for this purpose.
    To add entry at the beginning and deletion at the end to maintain the size of cache, 
    we can use doubly linked list. My solution uses the combination of both.

Time Complexity:
    get and set both methods use constant time to do the job. The time complexity is O(1)
    get - does a lookup using dictionary so the lookup time in O(1)
    set - does the insertion is constant time
Space Complexity: O(n)
    At maximum, we need n (max capacity) node in out dictionary to manage this cache.
"""
