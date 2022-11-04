import sys
from array import *
queue=array('i',[])
def enqueue ():
    element=int(input("Element element : "))
    queue.append(element)
    print(element," is added to queue ")
def dequeue():
    if not queue:
        print("Queue is added")
    else:
        e=queue.pop(0)
        print("Removed element is ",e)
def display():
    print("The elements is the Queue are :")
    for i in queue : print(i)
while True:
    choice=int(input("Choose one :\n1.Add 2.Remove 3.Show 4.Quit\n"))
    if choice ==1: enqueue()
    elif choice==2:dequeue()
    elif choice==3:display()
    elif choice==4:
        print("Exiting")
        break
    else: print("Choose correct choice !")
