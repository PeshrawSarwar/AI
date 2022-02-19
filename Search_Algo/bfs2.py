graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}
visited = []
queue = []
goal = 'F'

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  while queue:
      s=queue.pop(0)
      print(s)
      for neighbor in graph[s]:
          if neighbor not in visited:
              visited.append(neighbor)
              queue.append(neighbor)
              if goal in visited:
                  break


bfs(visited, graph, "A")

