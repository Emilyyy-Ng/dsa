class Node:
    def __init__(self, data: int):
        self.data = data
        self.lson: Node | None = None
        self.rson: Node | None = None

    def __repr__(self) -> str:
        return f"Node({self.data})"