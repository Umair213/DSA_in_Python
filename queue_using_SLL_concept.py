class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.items_count = 0

    def is_empty(self):
        return self.items_count == 0

    def insert_at_last(self, item):
        # No node
        if self.is_empty():
            self.head = self.tail = Node(item)
            self.items_count += 1
            return
        # One node
        if self.head == self.tail:
            self.tail = self.head.next = Node(item)
            self.items_count += 1
        # Multiple nodes
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            self.tail = temp.next = Node(item)
            self.items_count += 1
        return self.tail.item

    def enqueue(self, item):
        return self.insert_at_last(item)

    def delete_from_first(self):
        if not self.is_empty():
            deleted_item = self.head.item
            if self.head == self.tail:
                self.head = self.tail = None
                self.items_count -= 1
            else:
                self.head = self.head.next
                self.items_count -= 1
            return deleted_item
        return None

    def dequeue(self):
        return self.delete_from_first()

    def get_front(self):
        return self.head.item

    def get_rear(self):
        return self.tail.item

    def size(self):
        return self.items_count


queue_object = Queue()
print(queue_object.is_empty())
queue_object.enqueue(10)
queue_object.enqueue(20)
queue_object.enqueue(30)
print(queue_object.is_empty())
print(queue_object.get_front())
queue_object.delete_from_first()
print(queue_object.get_front())
print(queue_object.get_rear())
print(queue_object.size())
