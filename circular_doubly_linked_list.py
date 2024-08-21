class Node:
    def __init__(self, prev=None, item=None, next=None) -> None:
        self.prev = prev
        self.item = item
        self.next = next

class CDLL:
    def __init__(self, head=None) -> None:
        self.head = head
    
    def is_empty(self):
        return self.head == None
    
    def insert_at_start(self, item=None):
        # If CDLL is empty
        if self.is_empty():
            node = Node(item=item)
            node.prev = node
            node.next = node
            self.head = node
        # If CDLL has one node
        elif self.head == self.head.next:
            node = Node(self.head, item, self.head)
            # self.head.prev = self.head
            # self.head.next = self.head
            self.head.prev = self.head.next = node
            self.head = node
        # If CDLL has multiple nodes
        else:
            node = Node(self.head.prev, item, self.head)
            self.head.prev.next = node
            self.head.prev = node
            self.head = node

    def insert_at_last(self, item=None):
        if self.is_empty():
            node = Node(item=item)
            node.prev = node
            node.next = node
            self.head = node
        elif self.head == self.head.next:
            node = Node(self.head, item, self.head)
            self.head.prev = self.head
            self.head.next = self.head
        else:
            node = Node(self.head.prev, item, self.head)
            self.head.prev.next = node
            self.head.prev = node

    def search(self, item=None):
        if self.is_empty():
            return None
        temp = self.head
        # If single node in CDLL
        if temp.item == item:
            return temp
        # if last node
        if temp.prev.item == item:
            return temp.prev
        # If multiple nodes in CDLL
        while temp.next != self.head:
            if temp.item == item:
                return temp
            temp = temp.next

    def insert_after(self, node=None, item=None):
        while node is not None:
            if self.is_empty():
                return None
            # Only one node
            if self.head == self.head.next and self.head == self.head.prev and self.head == node:
                n = Node(self.head, item, self.head)
                self.head.prev = n
                self.head.next = n
                return
            # Last node
            if node == self.head.prev:
                n = Node(self.head.prev, item, self.head)
                self.head.prev.next = n
                self.head.prev = n
                return
            temp = self.head
            while temp.next != self.head:
                if temp == node:
                    n = Node(temp, item, temp.next)
                    temp.next.prev = n
                    temp.next = n
                    return
                temp = temp.next
        return None

    def print(self):
        if not self.is_empty():
            temp = self.head
            # For a single node
            if temp.next == self.head:
                print(temp.item)
                return
            while temp.next != self.head:
                print(temp.item, end=' ')
                temp = temp.next
            print(temp.item)

    def delete_first(self):
        if not self.is_empty():
            if self.head == self.head.next:
                self.head = None
            else:
                self.head.prev.next = self.head.next
                self.head.next.prev = self.head.prev
                self.head = self.head.next
        return None

    def delete_last(self):
        if not self.is_empty():
            if self.head == self.head.next:
                self.head = None
            else:
                self.head.prev.prev.next = self.head
                self.head.prev = self.head.prev.prev

    def delete_item(self, item):
        if not self.is_empty():
            # If last node
            if self.head.prev.item == item:
                self.head.prev.prev.next = self.head
                self.head.prev = self.head.prev.prev
            # If only node
            if self.head.item == item and self.head.next == self.head:
                self.head = None
            temp = self.head
            while temp.next != self.head:
                # If first node but not the only one
                if temp.item == item and temp == self.head:
                    self.head.prev.next = self.head.next
                    self.head.next.prev = self.head.prev
                    self.head = self.head.next
                # If node is in the middle
                if temp.item == item:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                temp = temp.next

    def __iter__(self):
        return CDLLIterator(self.head)

class CDLLIterator:
    def __init__(self, head) -> None:
        self.current = head  # Track the current node
        self.start = head     # Keep track of the start node
        self.first_pass = True  # A flag to handle the first iteration correctly

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None or (self.current == self.start and not self.first_pass):
            raise StopIteration

        self.first_pass = False  # After the first iteration, this flag is False
        item = self.current.item
        self.current = self.current.next  # Move to the next node

        return item
            


# Testing the above code below
my_list = CDLL()
my_list.insert_at_start(40)
my_list.insert_at_start(30)
my_list.insert_at_start(20)
my_list.insert_at_start(10)
my_list.insert_at_last(50)
my_list.print()
print("\n")
# my_list.insert_after(my_list.search(50), 60)
# my_list.insert_after(my_list.search(60), 70)
# my_list.delete_first()
# my_list.delete_last()
# my_list.delete_item(50)

my_list.print()
for i in my_list:
    print(i)