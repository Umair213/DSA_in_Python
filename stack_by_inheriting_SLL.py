from singly_linked_list import SLL

class Stack(SLL):
    def __init__(self) -> None:
        self.head = None
        self.item_count = 0
        self.tail = None

    def is_empty(self):
        return self.item_count == 0

    def push(self, item=None):
        if self.item_count == 0:
            self.head = self.insert_at_last(item)
        else:
            self.insert_at_last(item)
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            removed_item = self.delete_last_element()
            self.item_count -= 1
            return removed_item
        raise IndexError("Stack is already empty!")

    def peek(self):
        if not self.is_empty():
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            return temp.item
        return IndexError("Stack is empty!")

    def size(self):
        return self.item_count


stack_obj = Stack()
print(stack_obj.is_empty())
stack_obj.push(10)
stack_obj.push(20)
stack_obj.push(30)
print(stack_obj.peek())
stack_obj.pop()
# stack_obj.pop()
print(stack_obj.peek())
print(stack_obj.size())
print(stack_obj.is_empty())