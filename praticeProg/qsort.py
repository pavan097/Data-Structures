
def qsort(a):
    if len(a)>0:
        mid = a[0]
        right=[]
        left=[]
        for i in range(1,len(a)):
            if a[i] < mid:
                left.append(a[i])
                i+=1
            else:
                right.append(a[i])
                i+=1
        qsort(left)
        qsort(right)
        j=0
        if len(left)>0:
            for i in range(0,len(left)):
                a[j]=left[i]
                j+=1
                i+=1
        a[j]=mid
        j+=1
        if len(right)>0:
            for i in range(0,len(right)):
                a[j]=right[i]
                j+=1
                i+=1
        print(a)
#        print ('r ', left)
#        print ( 'm ', mid)
#        print ('l ',right)
    
if __name__=='__main__':
    
    a=[3,2,4,1,5,10,15,7,9,8,13,12,11]
    qsort(a)
