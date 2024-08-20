class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next

class CLL:
    def __init__(self, last=None) -> None:
        self.last = last

    def is_empty(self):
        return self.last == None

    def insert_at_start(self, item=None):
        node = Node(item)
        if self.last is None:
            node.next = node
            self.last = node
        else:
            node.next = self.last.next
            self.last.next = node

    def insert_at_last(self, item=None):
        node = Node(item)
        if self.last is None:
            node.next = node
            self.last = node
        else:
            node.next = self.last.next
            self.last.next = node
            self.last = node

    def search(self, item):
        if self.is_empty():
            return None
        if item == self.last.item:
            return self.last
        temp = self.last.next
        while temp != self.last:
            if item == temp.item:
                return temp
            temp = temp.next
        return None

    def insert_after(self, node=None, item=None):
        if node is not None:
            if node == self.last:
                node = Node(item, self.last.next)
                self.last.next = node
                self.last = node
            else:
                temp = self.last.next
                while temp != self.last:
                    if temp == node:
                        n = Node(item, temp.next)
                        temp.next = n
                    temp = temp.next

    def print(self):
        if not self.is_empty():
            temp = self.last.next
            # If there are more than one nodes in the Circular linked list
            if self.last != temp:
                while temp != self.last:
                    print(temp.item, end=' ')
                    temp = temp.next
                print(temp.item)

    def delete_first(self):
        if self.is_empty():
            return None
        if self.last == self.last.next:
            self.last = None
        else:
            self.last.next = self.last.next.next

    def delete_last(self):
        if self.is_empty():
            return None
        if self.last == self.last.next:
            self.last = None
        else:
            temp = self.last.next
            while temp.next != self.last:
                temp = temp.next
            temp.next = self.last.next
            self.last = temp

    def delete_item(self, item):
        if self.is_empty():
            return None
        if self.last == self.last.next and self.last.item == item:
            self.last = None
            return
        else:
            temp = self.last.next
            # For the first node
            if temp.item == item:
                self.last.next = temp.next
            while temp != self.last:
                if temp.next.item == item:
                    if temp.next == self.last:
                        temp.next = temp.next.next
                        self.last = temp
                        return
                    else:
                        temp.next = temp.next.next
                        return
                temp = temp.next

    def __iter__(self):
        if self.last == None:
            return CLLIterable(None)
        return CLLIterable(self.last.next)

class CLLIterable:
    def __init__(self, head):
        self.head = head
        self.first = head
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.head == None:
            raise StopIteration
        if self.head == self.first and self.count == 1:
            raise StopIteration
        self.count = 1
        item = self.head.item
        self.head = self.head.next

        return item






my_list = CLL()
# my_list.insert_at_last(10)
my_list.insert_at_start(30)
my_list.insert_at_start(100)
my_list.insert_at_start(120)
my_list.insert_at_last(150)
my_list.insert_after(my_list.search(150), 170)
my_list.print()
print("\n")
# my_list.delete_first()
# my_list.delete_last()
my_list.delete_item(120)
my_list.print()
for i in my_list:
    print(i)