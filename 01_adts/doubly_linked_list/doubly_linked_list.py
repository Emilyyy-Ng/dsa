from __future__ import annotations

class Node:
    def __init__(self, data: object):
        self.data = data
        self.next: Node | None = None
        self.prev: Node | None = None

    def __repr__(self) -> str:
        return f"Node({self.data})"

class DList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def insert_front(self, data: object) -> None:
        """Insert an element at the front of the linked list."""
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def append(self, data: object) -> None:
        """Append an element to the end of the linked list."""
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            return

        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def search(self, data: object) -> Node | None:
        """
        Return the target element in the linked list
        if it exists, and return None otherwise.
        """
        curr = self.head
        while curr:
            if curr.data == data:
                return curr
            curr = curr.next
        return None

    def remove(self, data: object) -> None:
        """Remove an element from the linked list."""
        # O(1) shortcut: remove tail directly if the list has multiple nodes.
        if self.tail and (self.head is not self.tail) and (self.tail.data == data):
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None
            return

        curr = self.head
        while curr:
            if curr.data == data:
                if curr.prev is not None:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next

                if curr.next is not None:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev
                return
            curr = curr.next

    def print(self) -> None:
        """Print the linked list in order."""
        if self.head is None:
            print("The linked list is empty.")
            return

        curr = self.head
        while curr:
            if curr.next:
                print(f"{curr.data} → ", end="")
            else:
                print(f"{curr.data}")
            curr = curr.next

if __name__ == "__main__":
    dll = DList()

    # Initialise the linked list
    for i in range(10):
        dll.append(i)
    dll.print()

    # Remove elements
    dll.remove(0) # remove the first element
    dll.remove(9) # remove the last element
    dll.print()

    # Search for element
    x = 1
    target = dll.search(x)
    if target:
        print(f"{x} is found: {target}.")
    else:
        print(f"{x} is not found.")