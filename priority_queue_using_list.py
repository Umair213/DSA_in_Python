class PriorityQueue:
    def __init__(self) -> None:
        self.pq = []

    def is_empty(self):
        return len(self.pq) == 0

    def push(self, item, priority):
        if self.is_empty():
            self.pq.append((item, priority))
            return
        index = 0
        if self.pq[index][1] > priority:
            self.pq.insert(index, (item, priority))
            return
        while index < len(self.pq) and self.pq[index][1] <= priority:
            index += 1
        self.pq.insert(index+1, (item, priority))
        return

    def pop(self):
        if not self.is_empty():
            self.pq.pop(0)
            return
        raise IndexError("No element in Priority Queue")

    def size(self):
        return len(self.pq)

    def get_front(self):
        if not self.is_empty():
            return self.pq[0][0]
        return None

    def get_rear(self):
        if not self.is_empty():
            return self.pq[-1][0]


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
