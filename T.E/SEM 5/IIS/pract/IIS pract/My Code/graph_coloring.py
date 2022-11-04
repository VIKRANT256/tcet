# Constraint
# Code: graph coloring


def solve():
    for i in color_states:
        # print(i)
        init_color = colors.copy()
        for j in neighbors[i]:
            if(color_states[j] != ''):
                # print(color_states[j])
                if(color_states[j] in init_color):
                    init_color.remove(color_states[j])
        color_states[i] = init_color[0]
    return color_states

colors = ['Red','Blue','Green']
states = ['Nagpur','Thane','Pune','Mumbai']
neighbors = {}
neighbors['Nagpur'] = ['Thane','Pune']
neighbors['Thane'] = ['Nagpur','Pune','Mumbai']
neighbors['Pune'] = ['Nagpur','Thane','Mumbai']
neighbors['Mumbai'] = ['Thane','Pune']

color_states = {'Nagpur': '',
                'Thane': '',
                'Pune': '',
                'Mumbai': ''}
# print(neighbors)

# N--------------T
# |             /|
# |           /  |
# |         /    |
# |       /      |
# |     /        |
# |   /          |
# | /            |
# P--------------M

solve()
print(color_states)