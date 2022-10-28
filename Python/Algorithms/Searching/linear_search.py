def linear_search(lst,key):
    flag = 0
    for i in lst:
        if i == key:
            print("Found at position {}".format(lst.index(i)+1))
            flag =1
    if flag == 0:
        print("Not Found")


# Driver Code
n=int(input("Enter the lenght of the list"))
l=[]
while True:
    for i in range (0,n):
        l.append(int(input))
    n1=int(input("Enter the no. to be searched"))
    linear_search(l,n1)



