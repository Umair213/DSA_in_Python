class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next

class SLL():
    def __init__(self, head=None) -> None:
        self.head = head

    def is_empty(self):
        if self.head == None:
            return True
        else:
            False

    def insert_at_start(self, value=None):
        node = Node(value, self.head)
        self.head = node

    def insert_at_last(self, value=None):
        node = Node(value)
        if not self.is_empty():
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node
            return node
        else:
            self.head = node
            return node

    def search(self, value=None):
        temp = self.head
        while temp is not None:
            if temp.item == value:
                return temp
            temp = temp.next
        # print(temp.item)

    def insert_after(self, node=None, value=None):
        if node is not None:
            if not self.is_empty():
                temp = self.head
                while temp != node:
                    if temp == None:
                        return None
                    temp = temp.next
                n = Node(value, temp.next)
                temp.next = n
        else:
            return None

    def print_all_elements(self):
        # if not self.is_empty():
        temp = self.head
        while temp != None:
            print(temp.item, end=' ')
            temp = temp.next

    def delete_first_element(self):
        if self.head is not None:
            self.head = self.head.next

    def delete_last_element(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            item = self.head
            self.head = None
            return item
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            item = temp.next
            temp.next = None
            return item

    def delete_item(self, item):
        if self.head is None:
            return
        elif self.head.next is None and self.head.item == item:
            self.head = None
        else:
            temp = self.head
            if temp.item == item:
                self.head = temp.next
                return
            while temp.next is not None:
                if temp.next.next is None and temp.next.item == item:
                    temp.next = None
                    return
                elif temp.next.item == item:
                    temp.next = temp.next.next
                temp = temp.next

    def __iter__(self):
        return SLLIterator(self.head)

# Making the following class to make our SLL iterable
class SLLIterator:
    def __init__(self, head):
        self.head = head
    def __iter__(self):
        return self
    def __next__(self):
        if not self.head:
            raise StopIteration
        item = self.head.item
        self.head = self.head.next
        return item



                

# Making an object to test all the above functions
# my_list = SLL()
# my_list.insert_at_start(20)
# my_list.insert_at_start(10)
# my_list.insert_at_last(30)
# my_list.insert_at_last(40)
# my_list.insert_after(my_list.search(40), 50)
# my_list.print_all_elements()
# print("\n")
# my_list.delete_first_element()
# my_list.delete_last_element()
# my_list.delete_item(30)
# my_list.print_all_elements()

# my_list.delete_item(10)
# print("\n")
# my_list.print_all_elements()
# for i in my_list:
#     print(i)

