class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next

class SLL:
    def __init__(self) -> None:
        self.head = None
        self.items_count = 0

    def is_empty(self):
        return self.head == None

    def insert_at_last(self, item):
        if self.is_empty():
            self.head = Node(item)
            self.items_count += 1
            return item
        else:
            if self.head.next is None:
                self.head.next = Node(item)
                self.items_count += 1
                return item
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = Node(item)
                self.items_count += 1
                return item

    def delete_first_element(self):
        if self.is_empty():
            return None
        if self.head.next is None:
            deleted_item = self.head.item
            self.head = None
            self.items_count -= 1
            return deleted_item
        else:
            temp = self.head
            if temp.next.next:
                while temp.next.next is not None:
                    temp = temp.next
                deleted_item = temp.next.item
                temp.next = None
                self.items_count -= 1
                return deleted_item
            


    def peek(self):
        if self.is_empty():
            return None
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        return temp.item

    def size(self):
        return self.items_count

class Stack:
    def __init__(self) -> None:
        self.sll_object = SLL()

    def is_empty(self):
        return self.sll_object.is_empty()

    def push(self, item):
        return self.sll_object.insert_at_last(item)

    def pop(self):
        return self.sll_object.delete_first_element()

    def peek(self):
        return self.sll_object.peek()

    def size(self):
        return self.sll_object.items_count

stack_object = Stack()
stack_object.is_empty()
stack_object.push(10)
stack_object.push(20)
stack_object.push(30)
print(stack_object.peek())
stack_object.pop()
print(stack_object.peek())
print(stack_object.size())