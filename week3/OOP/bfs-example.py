
graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }
'''
def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

print bfs(graph, '1', '11')
'''
def connection_level(self, panda1, panda2):
    queue = []
    queue.append([panda1])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == panda2:
            return path
        for adjacent in self.network.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
        return (len(queue)-1)
print connection_level(graph,'1', '7')