def partition(a,low,high):
    pivot=a[high]
    i=low=1
    for j in range(low,high):
        if a[j]<=pivot:
            i=i+1
            a[i+1],a[high]=a[high],a[i+1]
    return i+1
def quick_sort(a,low,high):
    if low<high:
        pi=partition(a,low,high)
        quick_sort(a,low,pi-1)
        quik_sort(a,pi+1,high)
a=[]
for i in range(int(input("enter the size:"))):
    a.append(int(input("enter the elements:")))
    quick_sort(a,0,len(a)-1)
print(a)
            
