from node import Node

class IterativeBST:
    def __init__(self):
        self.root = None

    def search(self, target: int) -> Node | None:
        """Return the target node if found, otherwise return None."""
        curr = self.root
        while curr:
            if target < curr.data:
                curr = curr.lson
            elif target > curr.data:
                curr = curr.rson
            else: # target == curr.data
                return curr
        return None

    def insert(self, data: int) -> None:
        """Insert a value into the tree."""
        node = Node(data)
        if self.root is None:
            self.root = node
            return

        parent = self.root
        curr = self.root
        while curr:
            parent = curr
            if data < curr.data:
                curr = curr.lson
            elif data > curr.data:
                curr = curr.rson
            else:
                raise ValueError(f"Cannot insert duplicate value {data} into the tree.")

        if data < parent.data:
            parent.lson = node
        elif data > parent.data:
            parent.rson = node

    def remove(self, target: int) -> None:
        """Remove a target value from the tree."""
        curr = self.root
        prev = None
        # Locate the target and track its parent node
        while curr:
            if target < curr.data:
                prev = curr
                curr = curr.lson
            elif target > curr.data:
                prev = curr
                curr = curr.rson
            else:
                break

        # Raise error if target not found
        if not curr:
            raise ValueError(f"Target value {target} does not exist in the tree.")

        # If target is an internal node, replace it by the min node in its right subtree
        if (curr.lson is not None) and (curr.rson is not None):
            node = curr.rson
            prev = curr
            while node.lson:
                prev = node
                node = node.lson

            if prev.rson == node:
                prev.rson = node.rson
            else:
                prev.lson = node.rson
            curr.data = node.data
        else: # 1-child or 0-child case: pick whichever child exists (or None if leaf)
            child = curr.lson if curr.lson is not None else curr.rson

            # Reconnect parent (prev) to child
            if prev is None:        # target was the root node
                self.root = child
            elif prev.lson == curr: # target was prev's left child
                prev.lson = child
            else:                   # target was prev's right child
                prev.rson = child

    def display(self) -> None:
        """Print tree as a list using in-order traversal."""
        print(self._in_order(self.root, []))

    # Helper
    def _in_order(self, curr: Node | None, res: list) -> list[int]:
        if curr is None:
            return res

        self._in_order(curr.lson, res)
        res.append(curr.data)
        self._in_order(curr.rson, res)

        return res

if __name__ == "__main__":
    tree = IterativeBST()

    # Initialise BST
    lst = [5, 2, 8, 1, 3, 6, 10, 7]
    for i in lst:
        tree.insert(i)

    print(f"Original tree:")
    tree.display()

    # Search for a node
    target_val = 5
    print(f"\nSearching for {target_val}...")
    target_node = tree.search(target_val)

    if target_node:
        print(f"{target_val} is found: {target_node}.")
    else:
        print(f"{target_val} is not found.")

    # Remove nodes
    for i in lst:
        print(f"\nRemoved {i}:")
        tree.remove(i)
        tree.display()