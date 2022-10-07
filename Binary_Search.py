def Binary_Search(l,low,high,key):
    while (low <= high):
        mid = (low+high)//2
        if l[mid] == key:
            return mid
        elif l[mid] > key:
            high = mid-1
        else:
            low = mid+1
    return -1
n=int(input("Enter the size of array:"))
low=0
l=[]
for i in range (0,n):
    ele = int(input("Enter the elements:"))
    l.append(ele)
print(l)
key = int(input("Enter the element that you want to search:"))
result = Binary_Search(l,low,n,key)
if result == -1:
    print("Element is not found")
else:
    print("Element is found at index:",result)
