class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class linklist:
    def __init__(self) -> None:
        self.head=None
    
    def insert_begin(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
            return 
        else:
            new_node.next=self.head
            self.head=new_node
    def printLL(self):
        curr_node=self.head
        while curr_node:
            print(curr_node.data)
            curr_node=curr_node.next




llist=linklist()
llist.insert_begin(5)
llist.insert_begin(6)
llist.insert_begin(7)

print('linklist')
llist.printLL()
        


    
        