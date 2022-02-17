# A* Search

graph = {
    'A': [('C', 6), ('B', 4), ('H', 7)],
    'B': [('D', 7), ('E', 13)],
    'C': [('G', 5), ('F', 8)],
    'F': [('H', 6)],
    'G': [('H', 6)],
}

# graph = [
#     ['A', 'C', 6],
#     ['A', 'B', 4],
#     ['A', 'H', 7],
#     ['A', 'B', 'D', 7],
#     ['A', 'B', 'E', 13],
#     ['A', 'B', 'D', 'E', 18],
#     ['A', 'C', 'G', 5],
#     ['A', 'C', 'F', 8],
#     ['A', 'C', 'G', 'H', 6],
#     ['A', 'C', 'F', 'H', 6],
# ]

def greedy(start, goal, graph, queue=[], visited=[]):
    if start not in visited:
        print(start)
        visited.append(start)

    queue = queue + [i for i in graph[start] if i[0][0] not in visited]
    queue.sort(key=lambda x: x[1])
    if queue[0][0] == goal:
        print(queue[0][0])
    else:
        p=queue[0]
        queue.remove(p)
        greedy(p[0], goal, graph, queue, visited)

greedy('A', 'H', graph)