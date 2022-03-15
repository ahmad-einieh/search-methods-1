dict_graph = {}

with open('cities.txt', 'r') as f:
    for l in f:
        city_a, city_b, p_cost = l.split()
        if city_a not in dict_graph:
            dict_graph[city_a] = {}
        dict_graph[city_a][city_b] = float(p_cost)
        if city_b not in dict_graph:
            dict_graph[city_b] = {}
        dict_graph[city_b][city_a] = float(p_cost)


def BreadthFirstSearch(graph, src, dst):
    max = 0
    q = [(src, [src], 0)]
    visited = {src}
    if len(q) > max:
        max = len(q)
    if src == dst:
        return src, 0, len(visited), max
    while q:
        if len(q) > max:
            max = len(q)
        (node, path, cost) = q.pop(0)
        for temp in list(graph[node].keys()):
            if len(q) > max:
                max = len(q)
            if temp == dst:
                return path + [temp], cost + graph[node][temp], len(visited), max
            else:
                if temp not in visited:
                    visited.add(temp)
                    q.append((temp, path + [temp], cost + graph[node][temp]))


def IterativeDeepening(graph, src, dst):
    level = 0
    count = 0
    max = 0
    stack = [(src, [src], 0)]
    visited = {src}
    if len(stack) > max:
        max = len(stack)
    if src == dst:
        return src, 0, len(visited), max
    while True:
        if len(stack) > max:
            max = len(stack)
        level += 1
        while stack:
            if len(stack) > max:
                max = len(stack)
            if count <= level:
                count = 0
                (node, path, cost) = stack.pop()
                for temp in list(graph[node].keys()):
                    if len(stack) > max:
                        max = len(stack)
                    if temp == dst:
                        return path + [temp], cost + graph[node][temp], len(visited), max
                    else:
                        if temp not in visited:
                            visited.add(temp)
                            count += 1
                            stack.append((temp, path + [temp], cost + graph[node][temp]))
            else:
                q = stack
                if (len(q) > max):
                    max = len(q)
                visited_bfs = {src}
                while q:
                    if (len(q) > max):
                        max = len(q)
                    if (len(stack) > max):
                        max = len(stack)
                    (node, path, cost) = q.pop(0)
                    for temp in list(graph[node].keys()):
                        if (len(q) > max):
                            max = len(q)
                        if (len(stack) > max):
                            max = len(stack)
                        if temp == dst:
                            return path + [temp], cost + graph[node][temp], len(visited) + len(visited_bfs), max
                        else:
                            if temp not in visited_bfs:
                                visited_bfs.add(temp)
                                q.append((temp, path + [temp], cost + graph[node][temp]))
                break


def ucsHelper(item):
    return item[2]


def ucs(graph, src, dst):
    max = 0
    q = [(src, [src], 0)]

    visited = {src}
    if len(q) > max:
        max = len(q)
    if src == dst:
        return src, 0, len(visited), max
    while q:
        if len(q) > max:
            max = len(q)
        (node, path, cost) = q.pop(0)
        for temp in list(graph[node].keys()):
            if len(q) > max:
                max = len(q)
            if temp == dst:
                return path + [temp], cost + graph[node][temp], len(visited), max
            else:
                if temp not in visited:
                    visited.add(temp)

                    q.append((temp, path + [temp], cost + graph[node][temp]))
                    q.sort(key=ucsHelper)


print(dict_graph['Adham'].keys())