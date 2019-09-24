import sys

class bsort:
    def __init__(self,l):
        self.lst = a
    def bubblesort(self):
        temp=0
        for i in range(0,len(self.lst)):
            for j in range(0,len(self.lst)):
                if (j+1) < len(self.lst):
                    if self.lst[j] > self.lst[j+1]:
                        temp = self.lst[j]
                        self.lst[j] = self.lst[j+1]
                        self.lst[j+1] = temp
                    
if __name__ == "__main__":
    if sys.argv[1] != '' or ' ':
        a = [int(i) for i in (sys.argv[1]).split(',')]
    else:
        a = [4,1,7,3,8,2]
    s = bsort(a)
    s.bubblesort()
