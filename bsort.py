a=[5,1,4,3,2,9,7,10,6,12,11]
temp=0
for i in range(0,len(a)):
    for j in range(0,len(a)):
        #print(a)
        if (j+1) < len(a):
            if a[j]>a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
            
print (a)