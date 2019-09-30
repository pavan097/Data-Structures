
class node:
    def __init__(self, data=None):
        self.data = data
        self.right = None

class linked:
    def __init__(self):
        self.head = None
    def insert(self, data):
        if self.head == None:
            self.head = node(data)
            return
        n = self.head
        while n.right is not None:
            n = n.right
        n.right = node(data)
    def display(self):
        if self.head == None:
            print('No data')
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.right



if __name__ == "__main__":
    l = linked()
    l.insert(5)
    l.insert(6)
    l.display()
    
