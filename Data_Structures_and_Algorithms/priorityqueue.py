import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push("task1", priority=1)
    pq.push("task2", priority=3)
    pq.push("task3", priority=2)

    print(pq.pop())  
    print(pq.pop())  
    print(pq.pop())  