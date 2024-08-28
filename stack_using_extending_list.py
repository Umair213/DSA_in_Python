class Stack(list):

    def is_empty(self):
        return len(self) == 0

    def push(self, item=None):
        super().append(item)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is already empty!")

    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is already empty!")

    def size(self):
        return len(self)

    def insert(self, item):
        raise AttributeError("No attribute insert in Stack")


stack_obj = Stack()
stack_obj.push(10)
stack_obj.push(20)
stack_obj.push(30)
print(stack_obj.peek())
print(stack_obj.size())
# print(stack_obj.insert(22))