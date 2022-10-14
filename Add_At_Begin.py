class Node:
    def __init__ (self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__ (self):
        self.head=None
    def Print_ll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
ll1=LinkedList()
ll1.add_begin(19)
ll1.add_begin(39)
ll1.add_begin(25)
ll1.Print_ll()
