class Stack:
    def __init__(self, capacity: int = 8):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        self.capacity = capacity
        self.size = 0
        self.stack: list[object | None] = [None] * capacity

    def push(self, data: object) -> None:
        """Append an element to the stack."""
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        self.stack[self.size] = data
        self.size += 1

    def pop(self) -> object:
        """Remove and return the last element."""
        if self.size == 0:
            raise IndexError("Stack is empty.")

        idx = self.size - 1
        out = self.stack[idx]
        self.stack[idx] = None
        self.size -= 1

        # Shrink if needed
        if self.size <= self.capacity // 4 and self.capacity >= 8:
            self._resize(self.capacity // 2)
        return out

    def peek(self) -> object:
        """Peek at the last element without removing it."""
        if self.size == 0:
            raise IndexError("Stack is empty.")
        return self.stack[self.size - 1]

    def _resize(self, new_capacity: int) -> None:
        """Increase / decrease the capacity of the stack."""
        temp: list[object | None] = [None] * new_capacity
        for i in range(self.size):
            temp[i] = self.stack[i]
        self.stack = temp
        self.capacity = new_capacity

    def is_empty(self) -> bool:
        return self.size == 0

if __name__ == "__main__":
    # ----- Using Custom Stack -----
    print("===== Custom Stack =====")
    s_custom = Stack(10)

    print("Input order:")
    for i in range(5):
        s_custom.push(i)
        print(i, end=" ")

    print(f"\nThe last element is {s_custom.peek()}.")

    print("\nOutput order:")
    while not s_custom.is_empty():
        print(s_custom.pop(), end=" ")

    # ----- Using Python's Built-in Functions -----
    print("\n\n===== Built-in Stack =====")
    s_builtin = []

    print("Input order:")
    for i in range(5):
        s_builtin.append(i)
        print(i, end=" ")

    print(f"\nThe last element is {s_builtin[-1]}.")

    print("\nOutput order:")
    while s_builtin:
        print(s_builtin.pop(), end=" ")

    print()