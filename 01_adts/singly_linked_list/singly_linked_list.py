from __future__ import annotations

class Node:
    def __init__(self, data: object):
        self.data = data
        self.next: Node | None = None

class SList:
    def __init__(self):
        self.head: Node | None = None

    def search(self, data: object) -> bool:
        if self.head is None:
            return False

        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    def insert_front(self, data: object) -> None:
        node = Node(data)
        if self.head is None:
            self.head = node
            return

        node.next = self.head
        self.head = node
        return

    def append(self, data: object) -> None:
        node = Node(data)
        if self.head is None:
            self.head = node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def remove(self, data: object) -> None:
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        curr = self.head
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                return
            curr = curr.next

    def print(self) -> None:
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
    sll = SList()
    for i in range(5):
        sll.insert_front(i)
    sll.print()
    sll.append(999)
    sll.remove(4)
    sll.print()
    x = 3
    if sll.search(x):
        print(f"{x} is found.")
    else:
        print(f"{x} is not found.")


