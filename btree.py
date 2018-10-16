

class Node():
    
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
    def insert(self,data):
        a=[]
        i=0
        if self.data is not None:
            if self.left is None:
                self.left=Node(data)
                a.append(self.left)
            else:
                self.right=Node(data)
                a.append(self.right)
            if self.right is not None:
                a[i].insert()
                i+=1