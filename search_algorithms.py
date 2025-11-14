from collections import deque

def bfs_with_path(graph, start_node, goal_node):
    if start_node not in graph or goal_node not in graph:
        return None

    queue = deque([(start_node, [start_node])])
    visited = {start_node}

    while queue:
        current_node, path = queue.popleft()

        if current_node == goal_node:
            return path

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append((neighbor, new_path))

    return None

def dfs_with_path(graph, start_node, goal_node):
    if start_node not in graph or goal_node not in graph:
        return None

    stack = [(start_node, [start_node])]
    visited = {start_node}

    while stack:
        current_node, path = stack.pop()

        if current_node == goal_node:
            return path

        for neighbor in reversed(graph.get(current_node, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                stack.append((neighbor, new_path))

    return None


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'H'],
        'D': ['B'],
        'E': ['B', 'F', 'I'],
        'F': ['C', 'E', 'G'],
        'G': ['F'],
        'H': ['C', 'J'],
        'I': ['E'],
        'J': ['H']
    }

    start = 'A'
    goal = 'J'

    print(f"Finding path from {start} to {goal} using BFS...")
    bfs_path = bfs_with_path(graph, start, goal)
    print(f"BFS Path: {bfs_path}")

    print(f"\nFinding path from {start} to {goal} using DFS...")
    dfs_path = dfs_with_path(graph, start, goal)
    print(f"DFS Path: {dfs_path}")
