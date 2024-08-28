class Node:
    def __init__(self, prev=None, item=None, next=None) -> None:
        self.prev = prev
        self.item = item
        self.next = next

class Deque:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0

    def insert_front(self, item):
        if self.head is None:
            self.head = self.tail = Node(None, item)
            self.item_count += 1
        else:
            node = Node(None, item, self.head)
            self.head.prev = node
            self.head = node
            if self.item_count == 1:
                self.tail = self.head.next
            self.item_count += 1

    def insert_rear(self, item):
        if self.tail is None:
            node = Node(None, item)
            self.tail = node
            self.item_count += 1
        else:
            node = Node(self.tail, item)
            self.tail.next = node
            self.tail = node
            self.item_count += 1

    def delete_front(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = self.tail = None
                self.item_count -= 1
            else:
                self.head = self.head.next
                self.head.prev = None
                self.item_count -= 1
        return None

    def delete_rear(self):
        if self.head is not None:
            if self.tail.prev is None:
                self.tail = self.head = None
                self.item_count -= 1
            else:
                self.tail = self.tail.prev
                self.tail.next = None
                self.item_count -= 1

    def get_front(self):
        if not self.is_empty():
            return self.head.item
        return None

    def get_rear(self):
        if not self.is_empty():
            return self.tail.item
        return None

    def size(self):
        return self.item_count

deque_object = Deque()
print(deque_object.is_empty())
deque_object.insert_front(10)
deque_object.insert_front(20)
deque_object.insert_rear(70)
print(deque_object.get_front())
deque_object.delete_front()
print(deque_object.get_front())
print(deque_object.get_rear())
deque_object.insert_rear(50)
print(deque_object.get_rear())