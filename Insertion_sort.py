def InsertionSort(a):
    for i in rangr(l,len(a)):
        key=a[i]
        j=i-1
        while  j>=0 and key<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
a=[]
for i in range(int(input("enter the size:"))):
    a.append(int(input("enter the element:")))
InsertionSort(a)
for i in range(len(a)):
    print(a[i])
