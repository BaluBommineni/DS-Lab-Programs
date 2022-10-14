import sys
from array import*
a=array('i',[])
while True:
    print("1.PUSH 2.POP 3.DISPLAY 4.EXIT ")
    ch=int(input("Enter your choice:"))
    if ch==1:
        ele=int(input("Enter element:"))
        a.append(ele)
        print("Inserted")
    elif ch==2:
        if len(a)==0:
            print("Stack is empty")
        else:
            print("Deleted element is",a.pop())
    elif ch==3:
        if len(a)==0:
            print("Stack is empty")
        else:
            print("The elements in stack is")
            for i in a:
                print(i)
    elif ch==4:
        sys.exit()
    else:
        print("Invalid choice")
