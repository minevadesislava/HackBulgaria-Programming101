class Graph:
    def _init_(self):
        self.graph = {}

    def has_node(self,node):
        return node in self.graph

    def add_edge(self,node_a, node_b):
        return  node_a in self.graph[node_b] and node_b in self.graph[node_a]

    def get_neighbors_for(self,node):
        if self.has_node(node):
            return [node for node in self.grapf[node]]
        return False
        

    def path_between(self, node_a, node_b):
        queue = []
        queue.append([node_a])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == node_b:
                return queue
            for adjacent in self.network.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
        return queue
        





