import random


city_destance =[
    #this is a distance of citys from a city to d city staring from A city
   # A B  C  D
    [0,5,10,20],
    [5,0,20,10],
    [10,20,0,5],
    [20,10,5,0]
]
def random_solution(city_destance):
    cities = list(range(len(city_destance)))
    solution = []
    for i in range(len(city_destance)):
            randomCity = cities[random.randint(0, len(cities) - 1)]
            solution.append(randomCity)
            cities.remove(randomCity)
    return solution
def routeLength(city_destance, solution):
    routeLength = 0
    for i in range(len(solution)):
        
        routeLength += city_destance[solution[i - 1]][solution[i]]
       
    return routeLength
def getNeighbours(chosen_solution):
    neighbours = []
    for i in range(len(chosen_solution)):
        for j in range(i + 1, len(chosen_solution)):
            neighbour = list(chosen_solution)
            neighbour[i] = chosen_solution[j]
            neighbour[j] = chosen_solution[i]
            neighbours.append(neighbour)
    return neighbours
def getBestNeighbour(city_destance, neighbours):
    bestRouteLength = routeLength(city_destance, neighbours[0])
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentRouteLength = routeLength(city_destance, neighbour)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
    return bestNeighbour, bestRouteLength
def hillClimbing(city_destance):
    currentSolution = random_solution(city_destance)
    currentRouteLength = routeLength(city_destance, currentSolution)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(city_destance, neighbours)

    while bestNeighbourRouteLength < currentRouteLength:
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(city_destance, neighbours)

    return currentSolution, currentRouteLength



print(hillClimbing(city_destance))