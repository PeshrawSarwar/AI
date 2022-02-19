from tkinter import N


graph = {
 'A' : ['B','C'],
 'B' : ['D', 'E'],
 'C' : ['F', 'G'],
 'D' : [],
 'E' : [],
 'F' : [],
 'G' : []
}
goal = 'F'
visited = set()

def dfs(graph, visited, node):
    if node not in visited:
       print(node)
       visited.add(node)
       for neighbor in graph[node]:
           if goal in visited:
               break
           else:
               dfs(graph, visited, neighbor)

dfs(graph, visited,"A")