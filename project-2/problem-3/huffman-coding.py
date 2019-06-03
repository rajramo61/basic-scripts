"""
Huffman Coding
A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding
schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each
character for each character. The Huffman code can be of any length and does not require a prefix;
therefore, this binary code can be visualized on a binary tree with each encoded character being stored
on leafs.

There are many types of pseudo code for this algorithm. At the basic core, it is comprised of building a
Huffman tree, encoding the data, and, lastly, decoding the data.

Here is one type of pseudo code for this coding schema:

Take a string and determine the relevant frequencies of the characters.
Build and sort a list of tuples from lowest to highest frequencies.
Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more
frequent letters. (This is the heart of the Huffman algorithm.)
Trim the Huffman Tree (remove the frequencies from the previously built tree).
Encode the text into its compressed form.
Decode the text from its compressed form.
"""

import sys
from queue import PriorityQueue



class HuffmanNode(object):
    def __init__(self, value=None, freq=0):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None
        self.is_left_visited = False
        self.is_right_visited = False


class Stack():
    def __init__(self):
        self.list = list()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    def is_empty(self):
        return len(self.list) == 0

    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s

        else:
            return "<stack is empty>"


def char_to_frequency_map(sequence):
    char_to_freq_map = {}
    for char in sequence:
        if char in char_to_freq_map:
            freq = char_to_freq_map.get(char).freq
            char_to_freq_map.get(char).freq = freq + 1
        else:
            char_to_freq_map[char] = HuffmanNode(char, 1)

    return char_to_freq_map


def load_data_to_priority_queue(map):
    q = PriorityQueue()
    for char in map:
        q.put(map.get(char).freq, map.get(char))

    return q


def create_parent_node_of_leaves(n1, n2):
    parent = HuffmanNode(None, n1.freq + n2.freq)
    parent.left = n1
    parent.right = n2
    return parent


def build_huffman_tree(q):
    while q.qsize() >= 1:
        parent = create_parent_node_of_leaves(q.get(), q.get())
        q.put(parent.freq, parent)

    return q.get()


def traverse_huffman_tree(node, stack, mapper, code_list):
    stack.push(node)
    if node.left and not node.is_left_visited:
        node.is_left_visited = True
        code_list.append(0)
        traverse_huffman_tree(node.left)
    elif node.right and not node.is_right_visited:
        node.is_right_visited = True
        code_list.append(1)
        traverse_huffman_tree(node.right)
    elif not node.left and not node.right:
        mapper[node.value] = ''.join(code_list)
        stack.pop()
        del mapper[-1]
    else:
        stack.pop()
        del mapper[-1]


def huffman_encoding(data):
    map = char_to_frequency_map(data)
    q = load_data_to_priority_queue(map)
    stack = Stack()
    char_code_mapper = {}
    code_list = []
    root_of_huffman_tree = build_huffman_tree(q)
    traverse_huffman_tree(root_of_huffman_tree, stack, char_code_mapper, code_list)
    for item in char_code_mapper:
        print(item, char_code_mapper.get(item))
    pass


def huffman_decoding(data,tree):
    pass


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))
    #
    # decoded_data = huffman_decoding(encoded_data, tree)
    #
    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))
