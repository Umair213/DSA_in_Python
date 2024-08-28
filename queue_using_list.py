class Queue:
    def __init__(self) -> None:
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            deleted_item = self.queue.pop(0)
            return deleted_item
        return None

    def get_front(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def get_rear(self):
        if not self.is_empty():
            return self.queue[-1]
        return None

    def size(self):
        return len(self.queue)


queue_object = Queue()
print(queue_object.is_empty())
queue_object.enqueue(10)
queue_object.enqueue(20)
queue_object.enqueue(30)
queue_object.enqueue(40)
print(queue_object.is_empty())
print(queue_object.get_front())
queue_object.dequeue()
print(queue_object.get_front())
print(queue_object.get_rear())
