lst=[1,2,3]

size_of_table=10
hash_table = [list() for _ in range(size)]

for i in range(len(lst)):
    index=int(i%size_of_table)
    ht[index]=a[i]
    
print(hash_table)
