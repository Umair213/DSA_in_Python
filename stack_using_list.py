class Stack:
    def __init__(self) -> None:
        self.lst = []

    def is_empty(self):
        return len(self.lst) == 0

    def push(self, item):
        self.lst.append(item)

    def pop(self):
        if not self.is_empty:
            return self.lst.pop()
        else:
            raise IndexError("Stack is already empty")

    def peek(self):
        if not self.is_empty():
            return self.lst[-1]
        else:
            raise IndexError("Stack is already empty")

    def size(self):
        return len(self.lst)


stack_obj = Stack()

print(stack_obj.is_empty())
stack_obj.push(10)
stack_obj.push(20)
print(stack_obj.peek())
print(stack_obj.size())
stack_obj.pop()
print(stack_obj.size())