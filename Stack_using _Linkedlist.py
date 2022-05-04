class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
        
# 1 2 3 4 5

    def insert_end(self,val):
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=Node(val)
        
    def insert(self,val):
        temp=self.head
        self.head=Node(val)
        self.head.next=temp
        
        
    def show(self):
        temp=l.head
        while(temp.next!=None):
            print(temp.data)
            temp=temp.next
        print(temp.data)
        
    def pop(self):
        self.head=self.head.next
    
    

l=Linkedlist()
print("Enter t")
t=int(input())
if(t==1):
    print("Enter first value to create a Linked list")
    l.head=Node(int(input()))
    print("Enter insert 3 values")
    l.insert(int(input()))
    l.insert(int(input()))
    l.insert(int(input()))
    print("Show")
    l.show()
    print("Pop")
    l.pop()
    print("Show")
    l.show()
