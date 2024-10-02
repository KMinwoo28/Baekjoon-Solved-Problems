class node():
    def __init__(self, data, left = '.', right = '.'):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return self.data.__str__()
def preorder(a):
    if a != '.':
        print(a.data, end = '')
        preorder(a.left)
        preorder(a.right)
def inorder(a):
    if a != '.':
        inorder(a.left)
        print(a.data, end = '')
        inorder(a.right)
def postorder(a):
    if a != '.':
        postorder(a.left)
        postorder(a.right)
        print(a.data, end = '')
        
T = int(input())
alpha = []
for i in range(26):
    alpha.append(chr(65+i))
nodes = []
for i in range(T):
    nodes.append(node(chr(65+i)))
for _ in range(T):
    a,b,c= map(str,input().split())
    if b != '.':
        nodes[alpha.index(a)].left = nodes[alpha.index(b)]
    if c != '.':
        nodes[alpha.index(a)].right = nodes[alpha.index(c)]
preorder(nodes[0])
print()
inorder(nodes[0])
print()   
postorder(nodes[0]) 