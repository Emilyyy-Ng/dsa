from node import Node

class RecursiveBST:
    def __init__(self):
        self.root = None

    def search(self, target: int) -> Node | None:
        """Return the target node if found, otherwise return None."""
        return self._r_search(target, self.root)

    # Helper function
    def _r_search(self, target: int, curr: Node | None) -> Node | None:
        if curr is None:
            return None

        if target < curr.data:
            return self._r_search(target, curr.lson)
        elif target > curr.data:
            return self._r_search(target, curr.rson)
        else:
            return curr

    def insert(self, data: int) -> None:
        """Insert a value into the tree."""
        self.root = self._r_insert(data, self.root)

    # Helper function
    def _r_insert(self, data: int, curr: Node | None) -> Node:
        if curr is None:
            return Node(data)

        if data < curr.data:
            curr.lson = self._r_insert(data, curr.lson)
        elif data > curr.data:
            curr.rson = self._r_insert(data, curr.rson)
        else:
            raise ValueError(f"Cannot insert duplicate value {data} into the tree.")

        return curr

    def remove(self, target: int) -> None:
        """Remove a target value from the tree."""
        self.root = self._r_remove(target, self.root)

    # Helper function
    def _r_remove(self, target: int, curr: Node | None) -> Node | None:
        if curr is None: # target is not found
            raise ValueError(f"Target value {target} does not exist in the tree.")
        elif target < curr.data:
            curr.lson = self._r_remove(target, curr.lson)
            return curr
        elif target > curr.data:
            curr.rson = self._r_remove(target, curr.rson)
            return curr
        else: # target == curr
            if curr.lson is not None and curr.rson is not None:
                curr.rson = self._remove_min(curr, curr.rson)
            elif curr.lson is not None:
                curr = curr.lson
            else:
                curr = curr.rson
        return curr

    def _remove_min(self, replace_target: Node, curr: Node) -> Node | None:
        if curr.lson is None: # curr is the min node
            replace_target.data = curr.data
            return curr.rson
        else:
            curr.lson = self._remove_min(replace_target, curr.lson)
            return curr

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
    tree = RecursiveBST()

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