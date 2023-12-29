class Node(object):
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

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
            new_node.next = self.head
            self.head = new_node
        else: 
            self.head = new_node

    def insert_last(self, value):
        new_node = Node(value)
        node = self.head
        if node is None:
            self.head = new_node
        else:
            while node is not None:
                last_node = node.next if node.next is not None else node
                node = node.next
            last_node.next = new_node

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
            previous_node = node
            node = node.next
        
        if not found:
            raise Exception(f"Target value ({target_value}) not found in linked list ({self}).")


    def remove_first(self):
        node = self.head
        if node is None:
            raise Exception("Linked list is empty.")
        self.head = node.next


if __name__ == "__main__":
    elements = ['a', 'b', 'c', 'd', 'e']

    llist = LinkedList()

    for element in elements:
        llist.insert_last(element)
    
    llist.insert_before('c', 'foo')

    print(llist)