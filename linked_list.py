# creating a linked list 

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
         
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):

        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("None")

    def delete_node(self,key):
            temp = self.head

            if temp and temp.data == key:
                self.head = temp.next
                return 
            

            prev = None

            while temp and temp.data!=key:
                prev= temp
                temp = temp.next

            if temp == None:
                print("node with this data doesnt exist")
                return 
            
            prev.next = temp.next


ll = LinkedList()

ll.insert_at_begin(9)
ll.insert_at_end(76)
ll.insert_at_begin(10)
ll.insert_at_begin(34)
ll.insert_at_end(8)
ll.display()

ll.delete_node(34)
ll.display()

ll.delete_node(76)
ll.display()

