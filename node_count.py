class Tree:
    def __init__(self, dt, left=None, right=None):
        self.dt = dt
        self.left = left
        self.right = right
        self.count = 0
        
    def insert(self, dt):
        if dt < self.dt:
            if self.left is None:
                self.left = Tree(dt)
            else:
                self.left.insert(dt)
        else:
            if self.right is None:
                self.right = Tree(dt)
            else:
                self.right.insert(dt)        

    def size(self,root):
        if root == None: return 0
        self.count+=1
        self.size(root.left)
        self.size(root.right)
        return self.count
    
root = Tree(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print('Total Number of Node: ',root.size(root))