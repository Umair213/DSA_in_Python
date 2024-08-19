class Node:
    def __init__(self, prev=None, item=None, next=None) -> None:
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, head=None) -> None:
        self.head = head

    def is_empty(self):
        if self.head is None:
            return True
        else:
            False

    def insert_at_start(self, item=None):
        if self.head is None:
            self.head = Node(None, item)
        else:
            node = Node(None, item, self.head)
            self.head.prev = node
            self.head = node

    def insert_at_last(self, item=None):
        if self.is_empty():
            self.head = Node(None, item)
        else:
            temp = self.head
            while temp is not None:
                if temp.next is None:
                    node = Node(temp, item, None)
                    temp.next = node
                    return
                temp = temp.next

    def search(self, item=None):
        # if self.is_empty():
        #     return None
        temp = self.head
        while temp is not None:
            if temp.item == item:
                return temp
            temp = temp.next
        return None

    def insert_after(self, node=None, item=None):
        if self.is_empty():
            return None
        temp = self.head
        while temp is not None:
            if temp == node:
                n = Node(temp, item, temp.next)
                if temp.next is not None:
                    temp.next.prev = n
                temp.next = n
                return
            temp = temp.next

    def print_items_in_DLL(self):
        if self.head is None:
            return None
        temp = self.head
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next

    def delete_first_element(self):
        if self.is_empty():
            return None
        temp = self.head
        if temp.next is None:
            self.head = None
        else:
            temp.next.prev = None
            self.head = temp.next
            temp.next.prev = None

    def delete_last_element(self):
        if self.is_empty():
            return None
        temp = self.head
        if temp.next is None:
            self.head = None
            return
        while temp is not None:
            if temp.next is None:
                temp.prev.next = None
                return
            temp = temp.next

    def delete_item(self, item=None):
        if self.is_empty():
            return None

        temp = self.head

        while temp is not None:
            if temp.item == item:
                # Case01: Only one Node
                if temp.prev is None and temp.next is None:
                    self.head = None
                # Case02: First Node of the Doubly linked list but not the only one
                elif temp.prev is None:
                    self.head = temp.next
                    temp.next.prev = None
                # Case03: Last Node of the Doubly linked list
                elif temp.next is None:
                    temp.prev.next = None
                # Case04: Node is in somewhere between the Doubly linked list
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                # Emptying the values of the pointers
                temp.next = None
                temp.prev = None
                return item
            temp = temp.next
        return None

    # To make Doubly linked list iterable, just like List Data type. 
    def __iter__(self):
        return DLLIterator(self.head)

class DLLIterator(DLL):
    def __init__(self, head=None) -> None:
        self.head = head
    def __iter__(self):
        return self
    def __next__(self):
        if not self.head:
            raise StopIteration
        item = self.head.item
        self.head = self.head.next
        return item


# Testing the above code below

my_list = DLL()
# my_list.insert_at_start(10)
# my_list.insert_at_start(100)
# my_list.insert_at_start(103)
# my_list.insert_at_start(19)
my_list.insert_at_last(50)
my_list.print_items_in_DLL()
# my_list.insert_at_start(15)
my_list.insert_after(my_list.search(510), 200)
my_list.delete_first_element()
my_list.print_items_in_DLL()
# my_list.delete_first_element()
# my_list.delete_last_element()
# my_list.delete_item(100)
print("\n")
my_list.print_items_in_DLL()
# for i in my_list:
#     print(i, end=" ")
