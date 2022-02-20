graph = {
    'B': [('A', 12), ('C', 10), ('E', 14)],
    'A': [('D', 6)],
    'D': [('H', 3)],
    'H': [('G', 0)],
    'C': [('D', 6), ('F', 4)],
    'F': [('H', 3)],
    'E': [('F', 4)],
}


def greedy(start, goal, graph, visited=[], queue=[]):
    if start not in visited:
       print(start)
       visited.append(start)

    queue = queue + [i for i in graph[start] if i[0][0] not in visited];
    queue.sort(key=lambda i: i[1])
    if queue[0][0] == goal:
        print(queue[0][0])
    else:
        p = queue[0];
        queue.remove(p)
        greedy(p[0], goal, graph, visited, queue)
greedy('B', 'G', graph)