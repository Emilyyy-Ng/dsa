from __future__ import annotations
from collections import deque

class Queue:
    def __init__(self, capacity: int = 8):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0.")
        self.queue: list[object | None] = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.size = 0

    def enqueue(self, data: object) -> None:
        """Append an element to the queue."""
        # Resize if the queue is full
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        idx = (self.front + self.size) % self.capacity
        self.queue[idx] = data
        self.size += 1

    def dequeue(self) -> object:
        """Remove and return the frontmost element in the queue."""
        if self.size == 0:
            raise IndexError("Queue is empty.")

        temp = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        # Resize if needed
        if self.size <= self.capacity // 4 and self.capacity >= 8:
            self._resize(self.capacity // 2)
        return temp

    def peek(self) -> object:
        """Peek at the frontmost element without removing it."""
        if self.size == 0:
            raise IndexError("Queue is empty.")

        return self.queue[self.front]

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return self.size == 0

    def _resize(self, new_capacity: int) -> None:
        """Increase / decrease the capacity of the queue."""
        temp: list[object | None] = [None] * new_capacity
        for i in range(self.size):
            temp[i] = self.queue[(self.front + i) % self.capacity]
        self.queue = temp
        self.capacity = new_capacity
        self.front = 0


if __name__ == "__main__":
    # ----- Using Custom Queue -----
    q_custom = Queue(10)
    print("===== Custom Queue =====")
    print("Input order:")
    for i in range(20):
        print(i, end=" ")
        q_custom.enqueue(i)

    print(f"\nThe frontmost element is {q_custom.peek()}.")

    print("\nOutput order:")
    while not q_custom.is_empty():
        print(q_custom.dequeue(), end=" ")

    # ----- Using Python's Standard Library -----
    q_std = deque()
    print("\n\n===== Standard Library (deque) =====")
    print("Input order:")
    for i in range(20):
        q_std.append(i)
        print(i, end=" ")

    # Peek at the first element
    print(f"\nThe frontmost element is {q_std[0]}.")

    print("\nOutput order:")
    while q_std:
        print(q_std.popleft(), end=" ")

    print()