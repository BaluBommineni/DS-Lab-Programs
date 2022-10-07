def mergesort(a):
    if len(a)>1:
        r=len(a)//2
        l=a[:r]
        m=a[r:]
        mergesort(l)
        mergesort(m)
        i=j=k=0
        while  i<len(l) and j<len(m):
            if l[i]<m[j]:
                a[k]=l[i]
                i+=1
            else:
                a[k]=m[j]
                j+=1
            k+=1
        while i<len(l):
            a[k]=l[i]
            i+=1
            k+=1
        while j<len(m):
            a[k]=m[j]
            j+=1
            k+=1
def printlist(a):
    for i in range(len(a)):
        print(a[i])
a=[]
for i in range(int(input("Enter size:"))):
    a.append(int(input("Enter element:")))


