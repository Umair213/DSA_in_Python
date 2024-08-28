class Deque:
    def __init__(self) -> None:
        self.deque = []

    def is_empty(self):
        return len(self.deque) == 0

    def insert_front(self, item):
        self.deque.insert(0, item)

    def insert_rear(self, item):
        self.deque.append(item)

    def delete_front(self):
        if not self.is_empty():
            self.deque.pop(0)
        return None

    def delete_rear(self):
        if not self.is_empty():
            self.deque.pop()
        return None

    def get_front(self):
        if not self.is_empty():
            return self.deque[0]
        return None

    def get_rear(self):
        if not self.is_empty():
            return self.deque[-1]
        return None
    

    def size(self):
        return len(self.deque)

deque_object = Deque()
print(deque_object.is_empty())
deque_object.insert_front(10)
deque_object.insert_front(20)
print(deque_object.get_front())
deque_object.delete_front()
print(deque_object.get_front())
print(deque_object.get_rear())
deque_object.insert_rear(50)
print(deque_object.get_rear())