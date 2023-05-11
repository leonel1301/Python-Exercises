"""swap ends(D): Swap the first and last items in the sequence in D in O(1) time"""
"""Se puede intercambiar el primer y el último elemento de la lista simplemente eliminando ambos
 extremos en tiempo O(1) y luego insertándolos nuevamente en el orden opuesto,
también en tiempo O(1). Este algoritmo es correcto por las definiciones de estas operaciones."""


class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_first(self, data):
        if self.is_empty():
            self.head = self.tail = Node(data)
        else:
            new_node = Node(data, next=self.head)
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_last(self, data):
        if self.is_empty():
            self.head = self.tail = Node(data)
        else:
            new_node = Node(data, prev=self.tail)
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        data = self.head.data
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return data

    def delete_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        data = self.tail.data
        if self.head is self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return data

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


def shift_left(D, k):
    if (k < 1) or (k > len(D) - 1):
        return
    x = D.delete_first()
    D.insert_last(x)
    shift_left(D, k - 1)


linked_list = DoublyLinkedList()
for element in [1, 2, 3, 4, 5]:
    linked_list.insert_last(element)

shift_left(linked_list, 2)

print(linked_list.to_list())
