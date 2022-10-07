def countingSort(a,er):
    n=len(a)
    output=[0]*(n)
    count=[0]*(10)
    for i in range(0,n):
        index=a[i]
        count[index % 10]+=count[i-1]
    for i in range(1,10):
        count[i]+=count[i-1]
    i=n-1
    while i>=0:
        index=a[i]
        output[count[index%10]-1]=a[i]
        count[index%10]-=1
        i-=1
    i=0
    for i in range(0,len(a)):
        a[i]=output[i]
def radixSort(a):
    max1=max(a)
    exp=1
    while max1/exp>=1:
        countingSort(a,exp)
        exp*=10
a=[]
for i in range(int(input("Enter size:"))):
    a.append(int(input("Enter elements:")))
radixSort(a)
for i in range(len(a)):
    print(a[i])
        
