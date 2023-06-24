class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None


class Dll:
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
                else:
                    print(temp.data,"<->",end="")
                temp = temp.next

    def insert_begin(self,data):
        new_node = Node(data)
        temp = self.head
        temp.prev= new_node
        new_node.next = temp
        self.head = new_node

    def insert_last(self,data):
        new_node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp.next

    def insert_middle(self,pos,data):
        new_node = Node(data)
        temp = self.head
        for i in range(0,pos-1):
            temp = temp.next
        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp_next = new_node
        
    def delete_begin(self):
        temp = self.head
        self.head = temp.next
        temp.next.prev = None
        temp.next = None

    def delete_last(self):
        prev =self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None
        temp.prev = None
        
    def delete_middle(self,pos):
        prev = self.head
        temp = self.head.next
        for i in range(0,pos-1):
            prev = prev.next
            temp = temp.next
        prev.next = temp.next
        temp.prev = prev
        
obj = Dll()

node_1 = Node("sanjay")
obj.head = node_1

node_2 = Node("Abhinay")
node_1.next = node_2
node_2.prev = node_1.next

node_3 = Node("druva")
node_2.next = node_3
node_3.prev = node_2.next

node_4 = Node("suraj")
node_3.next = node_4
node_4.prev = node_3.next

node_5 = Node(" bharath")
node_4.next = node_5
node_5.prev = node_4.next

obj.display()






 
