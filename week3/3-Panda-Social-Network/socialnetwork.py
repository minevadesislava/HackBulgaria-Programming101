import json
from panda import Panda

class PandaSocialNetwork:
    def __init__(self):
        self.network = {}

    def add_panda(self, panda):
        if panda in self.network:
            raise Exception("PandaAlreadyThere") 

        self.network[panda] = []

    def has_panda(self, panda):
        return panda in self.network

    def make_friends(self, panda1, panda2):

        if not self.has_panda(panda1):
            self.add_panda(panda2)

        if not self.has_panda(panda2):
            self.add_panda(panda1)

        if self.are_friends(panda1,panda2):
            raise Exception("Pandas are already friends.")

        self.network[panda1].append(panda2)
        self.network[panda1].append(panda1)  

    def are_friends(self, panda1, panda2):
        return panda1 in self.network[panda2] and panda2 in self.network[panda1]

    def friends_of(self, panda):
        if self.has_panda(panda):
            return [panda for panda in self.pandas[panda]]
        return False

    def connection_level(self, panda1, panda2):
        queue = []
        queue.append([panda1])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == panda2:
                return len(queue)
            for adjacent in self.network.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
        return (len(queue)-1)


    def are_connected(self, panda1, panda2):
        if self.connection_level(panda1, panda2) > 0:
            return True
        else:
            return False


    def save(self, path):
        pandas_data = {}
        for panda in self.network:
            pandas_data[repr(panda)] = []
            for friend in self.network[panda]:
                pandas_data[repr(panda)] += [repr(friend)]

        json_string = json.dumps(pandas_data, indent=4)
        with open(path, "w") as save_file:
            save_file.write(json_string)

    def load(self, path):
        contents = {}
        with open(path, "r") as load_file:
            contents = json.loads(load_file.read())

        for panda in contents.keys():
            for friend in contents[panda]:
                if not self.are_friends(panda, friend):
                    self.make_friends(panda, friend)

        return self

network = PandaSocialNetwork()
ivo = Panda("Ivo", "ivo@pandamail.com", "male")
rado = Panda("Rado", "rado@pandamail.com", "male")
tony = Panda("Tony", "tony@pandamail.com", "female")
print rado

for panda in [ivo, rado, tony]:
    network.add_panda(panda)

network.make_friends(ivo, rado)
network.make_friends(rado, tony)

print(network.are_connected(ivo,rado))



