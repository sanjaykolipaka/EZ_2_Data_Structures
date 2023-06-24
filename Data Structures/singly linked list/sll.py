class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Sll:
    
    def __init__(self):
        self.head = None
        
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:

            temp = self.head
            while(temp):
                if(temp.next == None):
                    print(temp.data)
                    temp = temp.next
                else:
                    print(temp.data,"->",end="")
                    temp = temp.next
    def insert_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self,data):
        new_node = Node(data)
        temp = self.head
        while temp:
            temp = temp.next
        temp.next = new_node
        new_node.next = None
        
    def insert_middle(self,pos,data):
        new_node = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    
     
    def delete_begin(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def delete_end(self):
        prev = self.head
        temp =self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None


    def delete_middle(self,pos):
        prev  = self.head
        temp = self.head.next
        for i in range(pos-1):
            temp =temp.next
            prev = prev.next
        prev.next = temp.next

obj = Sll()

node_1 = Node(10)
obj.head = node_1

node_2 = Node(20)
node_1.next = node_2

node_3 = Node(30)
node_2.next = node_3

node_4 = Node(40)
node_3.next = node_4


