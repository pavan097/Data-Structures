
a=[]
i=0

class Q:
    
    global a
    def enq(self,data):
        a.append(data)
        
    def deq(self):
        global i
        self.temp=a[i]
        i=i+1
    
    def print(self):
        for j in range(i,len(a)):
            print(a[j])
        
b=Q()

b.enq(5)
b.deq()
b.enq(6)
b.print()