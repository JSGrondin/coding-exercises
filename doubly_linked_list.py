"""
The Node and LinkedList classes together implement a doubly linked list
data structure. The Node class represents an individual node in a linked list, 
containing data and a reference to the next and previous node. The LinkedList 
class provides a collection of connected nodes, allowing for operations like
insertion, deletion, and traversal.

Compared to the singly linked list, the Node class has an additional previous 
attribute, and the LinkedList class has an additional tail attribute, which enables
running insert_last and remove_last in O(1) instead of O(n).

LinkedList Methods:
- insert_first(self, value): Inserts a new node at the beginning of the list. Time Complexity: O(1)
- insert_last(self, value): Inserts a new node at the end of the list. Time Complexity: O(n)
- insert_after(self, target_value, new_value): Inserts a new node after a node with the target value. Time Complexity: O(n)
- insert_before(self, target_value, new_value): Inserts a new node before a node with the target value. Time Complexity: O(n)
- remove_first(self): Removes the first node of the list. Time Complexity: O(1)
- remove_last(self): Removes the last node of the list. Time Complexity: O(n)
- reverse(self): Reverses the list in place. Time Complexity: O(n)
- remove(self, value): Removes all nodes with the specified value. Time Complexity: O(n)
"""

class Node(object):
    def __init__(self, value):
        self.data = value
        self.next = None
        self.previous = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.data)
        return " -> ".join(nodes)

    def insert_first(self, value):
        new_node = Node(value)
        if self.head:
            first_node = self.head
            first_node.previous = new_node
            new_node.next = first_node
            self.head = new_node
        else: 
            self.head = new_node
            self.tail = new_node

    def insert_last(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            last_node = self.tail
            last_node.next = new_node
            new_node.previous = last_node
            self.tail = new_node

    def insert_after(self, target_value, new_value):
        # Will insert node with new_value after every node with
        # target value.
        node = self.head
        if node is None:
            raise Exception("Linked list is empty.")
        
        found = False
        new_node = Node(new_value)
        while node is not None:
            if node.data == target_value:
                found = True
                new_node.next = node.next
                new_node.previous = node
                node.next = new_node
                node = new_node.next
            else:
                node = node.next
        
        if not found:
            raise Exception(f"Target value ({target_value}) not found in linked list ({self}).")

    def insert_before(self, target_value, new_value):
        # Will insert node with new_value before every node with
        # target value.
        node = self.head
        if node is None:
            raise Exception("Linked list is empty.")
        
        found = False
        new_node = Node(new_value)
        previous_node = None
        while node is not None:
            if node.data == target_value:
                found = True
                if previous_node is None:
                    self.insert_first(new_value)
                else:
                    previous_node.next = new_node
                    new_node.next = node
                    node.previous = new_node
            previous_node = node
            node = node.next
        
        if not found:
            raise Exception(f"Target value ({target_value}) not found in linked list ({self}).")

    def remove_first(self):
        node = self.head
        if node is None:
            raise Exception("Linked list is empty.")
        self.head = node.next
        self.head.previous = None
    
    def remove_last(self):
        node = self.tail
        if node is None:
            raise Exception("Linked list is empty.")
        self.tail = node.previous
        self.tail.next = None

    def reverse(self):
        node = self.head
        self.tail = node
        if node is None:
            raise Exception("Linked list is empty.")
        previous_node = None
        while node is not None:
            next_node = node.next
            node.next = previous_node
            node.previous = next_node
            self.head = node

            previous_node = node
            node = next_node

    def remove(self, value):
        # Will remove every nodes with specific value.
        node = self.head
        if node is None:
            raise Exception("Linked list is empty.")
        
        found = False
        previous_node = None
        while node is not None:
            if node.data == value:
                found = True
                if previous_node is None:
                    self.head = node.next
                    self.head.previous = None
                else:
                    previous_node.next = node.next
                    node.previous = previous_node
            previous_node = node
            node = node.next
        
        if not found:
            print(f"Value to be removed ({value}) not found in linked list ({self}).")

    def validate(self):
        node = self.head
        if node is None:
            raise Exception("Linked list is empty.")

        assert node.previous == None

        last_node = None
        while node is not None:
            assert node.previous == last_node
            
            last_node = node
            node = node.next
        
        assert self.tail == last_node


if __name__ == "__main__":
    elements = ['a', 'b', 'c', 'd', 'e']

    llist = LinkedList()

    for element in elements:
        llist.insert_last(element)
    
    llist.reverse()
    llist.validate()

    print(llist)