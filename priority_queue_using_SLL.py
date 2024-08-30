class Node:
    def __init__(self, item=None, priority=None, next=None) -> None:
        self.item = item
        self.priority = priority
        self.next = next

class PriorityQueue:
    def __init__(self) -> None:
        self.head = None
        self.item_count = 0

    def is_empty(self):
        return self.head == None

    def push(self, item, priority):
        node = Node(item, priority)
        if not self.head or self.head.priority > priority:
            node.next = self.head
            self.head = node
        else:
            temp = self.head
            while temp.next is not None and temp.priority <= priority:
                temp = temp.next
            node.next = temp.next
            temp.next = node


    def pop(self):
        if not self.is_empty():
            if self.head.next is None:
                self.head = None
                self.item_count -= 1
                return
            else:
                self.head = self.head.next
                self.item_count -= 1
                return
        raise IndexError("Priority Queue is empty!")

    def size(self):
        return self.item_count

    def get_front(self):
        return self.head.item

    def get_rear(self):
        if not self.is_empty():
            if self.head.next is None:
                return self.head.item
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                return temp.item
        return None


pq_obj = PriorityQueue()
print(pq_obj.is_empty())
pq_obj.push(10, 2)
pq_obj.push(20, 2)
pq_obj.push(30, 1)
print(pq_obj.get_front())
print(pq_obj.get_rear())
pq_obj.push(40, 3)
print(pq_obj.get_rear())
print(pq_obj.is_empty())

