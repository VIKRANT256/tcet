class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def DLS(root, l, t):
    if(root == None):
        return
    
    if(l == 0):
        return
    
    if(root.data == t):
        # print(root.data)
        return root.data
    
    x1 = DLS(root.left, l-1, t)
    if(x1 == t):
        return x1
    x2 = DLS(root.right, l-1, t)
    if(x2 == t):
        return x2

tree = Tree('S')
tree.left = Tree('A')
tree.right = Tree('B')

tree.left.left = Tree('C')
tree.left.right = Tree('D')

tree.right.left = Tree('I')
tree.right.right = Tree('J')

tree.left.left.left = Tree('E')
tree.left.left.right = Tree('F')

tree.left.right.left = Tree('G')

tree.right.left.left = Tree('H')

target = 'J'
x = DLS(tree, 2, target)

if(x == None):
    print("Element not found")
else:
    print("Element found :", x)


# TC: O(b^l)
# SC: S(b*l)