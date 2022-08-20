class Tree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def searchDLS(root, h, t):
    h -= 1
    if(h == -1):
        return 0
    if(root == None):
        return 0
    
    if(t == root.val):
        return root.val

    l = searchDLS(root.left, h, t)
    if (l != 0):
        return l
    r = searchDLS(root.right, h, t)
    if (r != 0):
        return r

    if(l == 0):
        return r
    else:
        return l

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)

root.left.left = Tree(4)
root.left.right = Tree(5)

root.right.left = Tree(6)
root.right.right = Tree(7)

h = 2
target = int(input("Enter target element : "))

x = searchDLS(root, h, target)

if(x == 0):
    x = -1
    print("Target element not found")
else:
    print("Target element found :", target)