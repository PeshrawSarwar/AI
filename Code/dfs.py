graph={
    "A": ["B","C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}

visited= set()
goal="F"

def dfs(graph, visited, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            if goal in visited:
                break
            else:
                dfs(graph,visited,neighbor)



print("Deepth First Search : ")
dfs(graph, visited, "A")
