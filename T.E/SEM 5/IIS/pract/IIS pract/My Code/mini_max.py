
class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


tree = Tree(-1)

tree.left = Tree(-1)
tree.right = Tree(-1)

tree.left.left = Tree(-1)
tree.left.right = Tree(-1)
tree.right.left = Tree(-1)
tree.right.right = Tree(-1)

tree.left.left.left = Tree(-1)
tree.left.left.right = Tree(-1)
tree.left.right.left = Tree(-1)
tree.left.right.right = Tree(-1)

tree.right.left.left = Tree(-1)
tree.right.left.right = Tree(-1)
tree.right.right.left = Tree(-1)
tree.right.right.right = Tree(-1)

tree.left.left.left.left = Tree(3)
tree.left.left.left.right = Tree(4)
tree.left.left.right.left = Tree(2)
tree.left.left.right.right = Tree(1)
tree.left.right.left.left = Tree(7)
tree.left.right.left.right = Tree(8)
tree.left.right.right.left = Tree(9)
tree.left.right.right.right = Tree(10)
tree.right.left.left.left = Tree(2)
tree.right.left.left.right = Tree(11)
tree.right.left.right.left = Tree(1)
tree.right.left.right.right = Tree(12)
tree.right.right.left.left = Tree(14)
tree.right.right.left.right = Tree(9)
tree.right.right.right.left = Tree(13)
tree.right.right.right.right = Tree(16)


x = 0
def a_b(root, h):
    global x
    if(h%2 == 1):
        mn_mx = False
    else:
        mn_mx = True


    if(root.data == None):
        return
    
    if(root.data != -1):
        return root.data
    
    l = a_b(root.left, h-1)
    r = a_b(root.right, h-1)
    # print(mn_mx, l, r, x)
    # print(mn_mx)
    
    if(mn_mx):
        mn_mx = False
        if(l < r):
            x = l
            return l
        else:
            x = r
            return r
    else:
        mn_mx = True
        if(l < r):
            x = r
            return r
        else:
            x = l
            return l


height = 5
x = a_b(tree, height)
print("optimal value:", x)

'''
TC: O(b^(d/2))
SC: S()
'''