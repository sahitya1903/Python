class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)
    
    def reverse(self):
        for i in range(len(self.items)//2):
            self.items[i],self.items[len(self.items)-i-1]=self.items[len(self.items)-i-1],self.items[i]

    def display(self):
        for i in range(len(self.items)):
            print(self.items[i],end=' ')
        print()

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.pop())  
    print(stack.peek()) 
    stack.display()
    print(stack.size()) 
    stack.reverse()
    stack.display()
