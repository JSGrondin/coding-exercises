"""
A binary heap is a data structure that takes the form of a complete binary tree. This
implementation is a min-heap, where the parent node has a value that is smaller or equal
to its child. 

Methods:
- insert: Adds a new value to the heap. Time Complexity: O(log n)
- validate: Validates the heap property throughout the entire heap. Time Complexity: O(n)
- del_min: Removes and returns the smallest element from the heap. Time Complexity: O(log n)
- min_child: Returns the index of the smaller child of a given node. Time Complexity: O(1)
- build_heap: Builds a heap from a list of elements. Time Complexity: O(n log n)
"""

class BinaryHeap(object):
    def __init__(self):
        self.heap = [0]  # Empty binary heap with single 0 element for simpler floor div.
        self.size = 0
    
    def __repr__(self):
        return str(self.heap[1:])  # Not including 0 when examining heap

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self._percup()
    
    def _percup(self):
        i = self.size
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                self._swap(i, i // 2)
                i = i // 2
            else:
                break
    
    def _swap(self, idx_a, idx_b):
        tmp = self.heap[idx_a]
        self.heap[idx_a] = self.heap[idx_b]
        self.heap[idx_b] = tmp
    
    def validate(self):
        for idx in range(2, self.size + 1):  # No need to verify that 1st element is larger than 0
            if self.heap[idx] < self.heap[idx // 2]:
                raise Exception(f"Element {self.heap[idx]} \
                    is smaller than {self.heap[idx // 2]} in {self}.")

    def del_min(self):
        min_val = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.size -= 1
        self._percdown()
        return min_val
    
    def _percdown(self):
        i = 1
        while i * 2 <= self.size:
            mc = self.min_child(i)
            if self.heap[i] > self.heap[mc]:
                self._swap(i, mc)
                i = mc
            else:
                break
    
    def min_child(self, i):
        "Returns index of minimum child, assumes there is at least one child."
        if 2 * i + 1 > self.size:
            return 2 * i
        elif self.heap[2 * i + 1] < self.heap[2 * i]:
            return 2 * i + 1
        else:
            return 2 * i
    
    def build_heap(self, element_list):
        for element in element_list:
            bheap.insert(element)
        return bheap


if __name__ == "__main__":
    elements = [20, 15, 8, 38, 71, 2, -1, 27]

    bheap = BinaryHeap()
    bheap.build_heap(elements)
    bheap.validate()

    bheap.del_min()

    print(bheap)