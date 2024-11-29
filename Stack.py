class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return len(self.stack) == 0
    def push(self,item):
        self.stack.append(item)
        print(f"{item} is pushed to stack")
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.pop()
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]
    def Size(self):
        return len(self.stack)

stack1 = Stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)
print(f"Size of the stack1 is {stack1.Size()}")
stack1.peek()
stack2 = Stack()
print(f"Stack2 is empty? {stack2.is_empty()}")
stack2.push(40)
stack2.peek()