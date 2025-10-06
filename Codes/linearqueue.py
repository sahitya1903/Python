class LinearQueue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full!")
        else:
            self.queue.append(item)
            print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            item = self.queue.pop(0)
            print(f"Dequeued: {item}")
            return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            return self.queue[0]

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue:", self.queue)

# Example usage:
if __name__ == "__main__":
    q = LinearQueue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.display()
    q.dequeue()
    q.display()
    print("Peek:", q.peek())