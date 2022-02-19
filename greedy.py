graph = {
    'B': [('E', 14), ('A', 12), ('C', 10)],
    'E': [('F', 4)],
    'C': [('F', 4), ('D', 6)],
    'A': [('D', 6)],
    'F': [('H', 3)],
    'D': [('H', 3)],
    'H': [('G', 0)]
}


def greedy(start, goal, graph, queue=[], visited=[]):
    if start not in visited:
        print(start)
        visited.append(start)

    queue = queue + [i for i in graph[start] if i[0][0] not in visited]
    queue.sort(key=lambda i:i[1])
    if queue[0][0] == goal:
        print(queue[0][0])
    else:
        p = queue[0]
        queue.remove(p)
        greedy(p[0], goal, graph, queue, visited)


greedy('B', 'G', graph)
