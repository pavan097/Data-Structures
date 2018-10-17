# lst=[1,2,3]
class  Hash():
    def insert(self,lst)
        size_of_table=10
        hash_table = [list() for _ in range(size_of_table)]

        for i in range(len(lst)):
            index=int(i%size_of_table)
            ht[index]=a[i]

        print(hash_table)
       
    def search(self,value):
        if value in hash_table:
            print('value is present in the hash table')
        else:
            print('value is not in hash table')
