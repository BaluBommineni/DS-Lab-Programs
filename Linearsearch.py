def LinearSearch(l,n,key):
    for i in range(0,n):
        if(l[i]==key):
            return i
    return -1
n=int(input("Enter the size of array:"))
l=[]
for i in range (0,n):
    ele = int(input("Enter the elements:"))
    l.append(ele)
print(l)
key = int(input("Enter the element that you want to search:"))
result = LinearSearch(l,n,key)
if result == -1:
    print("Element is not found")
else:
    print("Element is found at index:",result)
