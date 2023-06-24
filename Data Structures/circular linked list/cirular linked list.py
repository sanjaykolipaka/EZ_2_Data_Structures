class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

        
class Csll:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def display(self):
        i = 0
        if self.head is None:
            print("Linked List is empty")
        else:
            temp=self.head
            while(temp.next != self.head):
                print(temp.data,"->",end="")
                i = i+1
                temp=temp.next
            print(temp.data,"->",end="")
            temp=temp.next
            print(temp.data)
            print("length of list=",i+1)
        '''
        temp=self.head
        z=temp
        while(temp.next!=z):
            print(temp.data,"->",end="")
            temp=temp.next
        print(temp.data)
        '''
    def insert_beg(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next=self.head
            self.head = new_node
            self.tail.next = self.head
        
    def insert_last(self,data):
        temp=self.head
        new_node=Node(data)
        while(temp!=self.tail):
            temp=temp.next
        temp.next=new_node
        new_node.next=self.head
        self.tail=new_node

    def insert_middle(self,pos,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            if pos == 1:
                insert_beg(data)
            else:
                temp = self.head
                for i in range(0,pos-1):
                    temp = self.head
                new_node.next = temp.next
                temp.next = new_node
            


    def del_last(self):
        temp=self.head
        while(temp!=self.tail):
            temp=temp.next
        self.tail=temp
        temp.next=self.head

        
    def del_beg(self):
        temp=self.head
        while(temp!=self.tail):
            temp=temp.next
        temp.next=self.head.next
        self.head=self.head.next
        
    def del_mid(self,pos):
        if self.head is None:
            print("Circular Linked lista is Empty")
        elif pos == 1:
            del_last()
        else:
            prev = self.head
            temp = self.head.next
            for i in range(1,pos-1):
                prev = prev.next
                temp = temp.next
            prev.next = temp.next
        



        
        

obj=Csll()

node_1=Node(10)
obj.head=node_1

node_2=Node(20)
node_1.next=node_2

node_3=Node(30)
node_2.next=node_3

node_4=Node(40)
node_3.next=node_4
obj.tail=node_4

obj.tail.next=obj.head



