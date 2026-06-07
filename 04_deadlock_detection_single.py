"""
Topic 4: Deadlock Detection for Single-Instance Resource Types
Constructs a Resource Allocation Graph (RAG) and executes Cycle Detection 
using a Depth-First Search (DFS) traversal algorithm to catch deadlocks.
"""

class ResourceAllocationGraph:
    def __init__(self):
        # Adjacency list mapping: node -> list of directed edge destinations
        # Nodes can represent both Processes (e.g., 'P0') and Resources (e.g., 'R0')
        self.graph = {}

    def add_edge(self, source, destination):
        if source not in self.graph:
            self.graph[source] = []
        if destination not in self.graph:
            self.graph[destination] = []
        self.graph[source].append(destination)

    def _has_cycle_dfs(self, node, visited, recursion_stack):
        visited.add(node)
        recursion_stack.add(node)

        for neighbor in self.graph.get(node, []):
            if neighbor not in visited:
                if self._has_cycle_dfs(neighbor, visited, recursion_stack):
                    return True
            elif neighbor in recursion_stack:
                # If a neighbor is already in the active recursion stack, a cycle exists!
                return True

        recursion_stack.remove(node)
        return False

    def detect_deadlock(self):
        visited = set()
        recursion_stack = set()

        # Run cycle detection across all unvisited nodes in the graph topology
        for node in self.graph:
            if node not in visited:
                if self._has_cycle_dfs(node, visited, recursion_stack):
                    return True
        return False

if __name__ == "__main__":
    print("--- Deadlock Detection: Single-Instance Resource Type ---")
    rag = ResourceAllocationGraph()

    # Scenario: Building a circular dependency graph
    # P0 holds R0 and requests R1 -> R1 is allocated to P1 -> P1 requests R0
    rag.add_edge("R0", "P0")  # R0 is allocated to P0
    rag.add_edge("P0", "R1")  # P0 is requesting R1
    rag.add_edge("R1", "P1")  # R1 is allocated to P1
    rag.add_edge("P1", "R0")  # P1 is requesting R0 (Creates Cycle!)

    print("\nScanning Resource Allocation Graph for circular wait states...")
    if rag.detect_deadlock():
        print("CRITICAL ALTERT: Deadlock state DETECTED! A circular wait path exists in memory.")
    else:
        print("System State: SAFE. No circular dependencies found.")
