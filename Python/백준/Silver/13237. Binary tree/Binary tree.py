class node:
    def __init__(self,data,parent = None):
        self.data = data
        self.parent = parent
    def __str__(self):
        return self.data.__str__()
T = int(input())
nodes = []
for s in range(T):
    nodes.append(node(s))
for i in range(T):
    parent = int(input())
    if parent != -1:
        nodes[i].parent = nodes[parent-1]
for a in nodes:
    count = 0
    while a.parent != None:
        a = a.parent
        count += 1
    print(count)
