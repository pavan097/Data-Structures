def bubblesort(lst):
    temp=0
    for i in range(0,len(lst)):
        for j in range(0,len(lst)):
            if (j+1) < len(lst):
                if lst[j]>lst[j+1]:
                    temp = lst[j]
                    lst[j] = lst[j+1]
                    lst[j+1] = temp
                    
