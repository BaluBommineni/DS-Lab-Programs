class Node:
    def __init__(self,data):
        self.data = data
        self.nextRef = None
class LinkedList:
    def __init__(self):
        self.head = None
    def CreateLL(self,ele):
        newnode=Node(ele)
        print("Node is created")
        if (self.head is None):
            self.head=newNode
        else:
            ptr=self.head
            while (ptr.next is not None):
                ptr=ptr.next
                ptr.next=newNode
    def Print_ll(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            val = self.head
            while val:
                print(val.data)
                val = val.nextRef
    def AddatBegining(self,node=None,data=None):
        if data is None:
            if node is None:
                print("Node is empty")
                return
            node.nextRef = self.head
            self.head = node
            return
        else:
            newnode = Node(data)
            newnode.nextRef = self.head
            self.head = newnode

    def AddatMiddle(self,preNode=None,newnode=None,data = None):
        if data is None:
            if preNode is None:
                print("must give a previous node")
                return
            elif newnode is None:
                print("must give a inserting node")
                return
            newnode.nextRef = preNode.nextRef
            preNode.nextRef = newnode
            return
        newnode = Node(data)
        newnode.nextRef = preNode.nextRef
        preNode.nextRef = newnode



    def AddatEnd(self,newnode=None):
        if newnode is None:
            print("must give a inserting node")
            return
        if self.head == Node:
            self.head = newnode
            return
        last = self.head
        while last.nextRef:
            last = last.nextRef
        last.nextRef = newnode        
        

    def remove(self,key):
        if key is None:
            print("Data must be given")
            return    
        n = self.head
        if n.data==key:
            self.head = n.nextRef
        while n:
            prenode = n
            keynode = n.nextRef
            if keynode.data == key:
                prenode.nextRef = keynode.nextRef
                del keynode
                n = None
            else:
                n = n.nextRef
                
                

    def length(self):
        n = self.head
        l = 0
        while n:
            l += 1
            n = n.nextRef
        return l
    

    def find(self,key):
        keynode = self.head
        c = 0
        while keynode:
            c += 1
            if keynode.data == key:
                return c
            keynode = keynode.nextRef
            

    def getNode(self,nod_pos):
        keynode = self.head
        c = 0
        while keynode:
            c+=1
            if c == nod_pos:
                return keynode.data
            keynode = keynode.nextRef   


    def getNodeFormEnd(self,key):
        l = self.length()
        node_pos = l - key +1
        return self.getNode(node_pos)
ll1=LinkedList()
n=0
while n!=6:
    print("1: Add At Begin\n2: Add At End\n3: Add At Middle\n4. Remove (Key)\n5. Print Linked List\n6. End  ")
    n=int (input("Enter your choice : "))
    if (n==1):
        i=1
        data=int(input("Give Data : "))
        ll1.AddatBegining(i,data)
        i=i+1
    elif n==2:
        data=int(input("Give Data : "))
        ll1.AddatEnd(data)
    elif n==5:
        ll1.Print_ll1()
