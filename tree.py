# tree program

class Tree:
    def __init__(self,data):
        self.node = data
        self.left = None
        self.right = None
        print('initalize :',self.node)
        
    def create(self,n):
        x = True
        while x:
            if not self.left:
                self.left = Tree(n)
                print('left')
                x = False
                break
            if not self.right:
                self.right = Tree(n)
                print('right')
                x = False
                break
            
            
    def nodes(self):
        print('root :',self.node)
        if self.left:
            print('left :',self.left.node)
        if self.right:
            print('right :',self.right.node)


if __name__ == "__main__":
    print('starting')
    a = Tree(1)
    a.create(2)
    a.create(3)
    a.create(4)
    a.create(5)    
    a.create(6)
    a.create(7)
    a.create(8)
    a.nodes()