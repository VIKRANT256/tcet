def a_star(graph, huristic_value, start, end):
    queue = []
    queue.append(start)
    path_found.append(start)
    while(1):
        x = queue.pop(0)
        if(x == end):
            break
        cost = 100000000
        min_location = ""
        for i in graph[x]:
            current_location = i[0]
            if(cost > i[1] + huristic_value[current_location]):
                cost = i[1] + huristic_value[current_location]
                min_location = current_location
        queue.append(min_location)
        path_found.append(min_location)


graph = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 2)]
}

huristic_value = {
    'S': 5,
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 6,
    'G': 0
}

path_found = []

a_star(graph, huristic_value, 'S', 'D')

print(path_found)

'''

Q = S

Q = A, G

Q = B, C

Q = D, G

Q = G

'''