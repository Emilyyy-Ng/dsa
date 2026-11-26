from typing import Any

class Graph:
    def __init__(self, directed: bool = False, weighted: bool = False):
        # Maps vertex -> {neighbor: weight} (weight is 1 for unweighted)
        self.adj: dict[Any, dict[Any, float]] = {}
        self.directed = directed
        self.weighted = weighted

    def __str__(self) -> str:
        if not self.adj:
            return "Empty Graph"

        arrow = "->" if self.directed else "--"
        lines = []
        for v, neighbors in self.adj.items():
            if not neighbors:
                lines.append(f"{v}: (no edges)")
            elif self.weighted:
                formatted = ", ".join(f"{nb} (w={w})" for nb, w in neighbors.items())
                lines.append(f"{v} {arrow} {formatted}")
            else:
                formatted = ", ".join(str(nb) for nb in neighbors)
                lines.append(f"{v} {arrow} {formatted}")
        return "\n".join(lines)

    def add_vertex(self, v: Any) -> None:
        """Add a vertex to the graph if it does not already exist."""
        if v not in self.adj:
            self.adj[v] = {}

    def add_edge(self, u: Any, v: Any, weight: float = 1) -> None:
        """Add an edge from u to v (updates weight if edge already exists)."""
        if u == v:
            raise ValueError("Self-loops are not allowed.")

        self.add_vertex(u)
        self.add_vertex(v)

        w = weight if self.weighted else 1
        self.adj[u][v] = w
        if not self.directed:
            self.adj[v][u] = w

    def remove_edge(self, u: Any, v: Any) -> None:
        """Remove the edge from u to v."""
        if u not in self.adj or v not in self.adj[u]:
            raise ValueError(f"Edge ({u}, {v}) does not exist.")

        del self.adj[u][v]
        if not self.directed:
            del self.adj[v][u]

    def get_neighbours(self, v: Any) -> list[Any] | list[tuple[Any, float]]:
        """Return all neighbours of vertex v."""
        if v not in self.adj:
            raise KeyError(f"Vertex {v} does not exist.")
        if self.weighted:
            return list(self.adj[v].items())
        return list(self.adj[v].keys())

    def get_vertices(self) -> list[Any]:
        """Return all vertices of the graph."""
        return list(self.adj.keys())


if __name__ == "__main__":
    g = Graph(directed=False, weighted=True)
    g.add_edge(1, 2, weight=10)
    g.add_edge(2, 3, weight=3)
    print(g)
