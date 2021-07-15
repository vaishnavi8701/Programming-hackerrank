class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def Insert_begin(self,data):
        if(self.head.data==None):
            self.head=Node(data)
        else:
            temp=self.head
            self.head=Node(data)
            self.head.next=temp
        
    def Insert_end(self,data):
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=Node(data)
        
    def Insert_postion(self,pos,data):
        count=1
        temp=self.head
        if(pos==1):
            self.Insert_begin(data)
        else:
            while(temp.next!=None and count<pos):
                count+=1
                prev=temp
                temp=temp.next
            if(count==pos):
                prev_temp=prev.next
                prev.next=Node(data)
                prev.next.next=prev_temp
            else:
                print("Given position out of range \n")
        
    def print_LL(self):
        temp=self.head
        print("The linked list has ")
        while(temp.next!=None):
            print(temp.data,end=" -> ")
            temp=temp.next
        print(temp.data)
        
    def length_LL(self):
        temp=self.head
        count=1
        while(temp.next!=None):
            count+=1
            temp=temp.next
        return count
    
    def print_mid(self):
        temp=self.head
        count=self.length_LL()
        if(count==1):
            print("There is no middle element. Only one element present")
            print(" The element is ",temp.data)
        elif(int(count%2)==0):
            temp_count=1
            while(int(count/2)!=temp_count):
                temp_count+=1
                temp=temp.next
            print("As length of linked list is even ,The middle element is  ",temp.data,", ",temp.next.data)
        else:
            temp_count=1
            while(int(count/2)!=temp_count):
                temp_count+=1
                temp=temp.next
            print("As length of linked list is odd ,The middle element is  ",temp.next.data)
    
    def Insert_mid(self,data):
        temp=self.head
        count=self.length_LL()
        if(count==1):
            print("There is no middle element. Only one element present")
            temp.next=Node(data)
        else:
            temp_count=0
            while(int(count/2)!=temp_count):
                temp_count+=1
                prev=temp
                temp=temp.next
            prev_next=prev.next
            prev.next=Node(data)
            prev.next.next=prev_next
       
            
    def del_mid(self):
        temp=self.head
        count=self.length_LL()
        if(count==1):
            print("There is no middle element. Only one element present")
            print(" The element is ",temp.data)
            temp.data=None
        elif(int(count%2)==0):
            if(int(count/2)==1):
                temp.data=None
                temp.next=None
            else:
                temp_count=1
                while(int(count/2)!=temp_count):
                    temp_count+=1
                    prev=temp
                    temp=temp.next
                print("As length of linked list is even ,The middle element deleted is  ",temp.data,", ",temp.next.data)
                prev.next=temp.next.next
        else:
            temp_count=1
            while(int(count/2)!=temp_count):
                temp_count+=1
                temp=temp.next
            print("As length of linked list is odd ,The middle element deleted is  ",temp.next.data)
            temp.next=temp.next.next
            
    def print_reverse(self):
        temp=self.head
        l=[]
        while(temp.next!=None):
            l.append(temp.data)
            temp=temp.next
        l.append(temp.data)
        temp=self.head
        l.reverse()
        for i in l:
            temp.data=i
            temp=temp.next
            
    def find_pos_end(self,pos):
        self.print_reverse()
        temp=self.head
        count=1
        while(temp.next!=None and count<pos):
                count+=1
                temp=temp.next
        if(count==pos):
            print(temp.data)
        else:
            print("Given position out of range \n")
        self.print_reverse()
        
        
    def remove_duplicates(self):
        temp=self.head
        l=[]
        if(self.head.next==None):
            print("No duplicates found")
        else:
            while(temp.next!=None):
                if temp.data in l:
                    print(temp.next.data)
                    temp=temp.next
                    prev.next=temp
                else:
                    l.append(temp.data)
                    prev=temp
                    temp=temp.next
            if(temp.data in l):
                prev.next=None
        
print("Hi, let me create a linked list.  To create give a value \n")
print("Enter the data :")
N=int(input())
S=LinkedList()
S.head=Node(N)
while(1):
    print("\nPress given option \n 1.Insert at beginning \n 2.Insert at given position \n 3.Length of the linked list \n 4.Print the middle element of the linked list\n 5.Delete the middle element of the linked list\n 6.Add an element to the middle of the linked list \n 7.Remove duplicate elements from linked list  \n 8.Print kth node from the end linked list \n 9.Reverse a linked list \n 10.Print the linked list \n 11. Insert at end \n 12. Out of list \n ")
    print("Enter your option")
    case=int(input())
    if(case==1):
        print("Enter the data")
        val=int(input())
        S.Insert_begin(val)
        print("After inserting at beginning")
        S.print_LL()
    elif(case==2):
        print("Enter the position to enter data")
        pos=int(input())
        print("Enter the data")
        val=int(input())
        S.Insert_postion(pos,val)
        print("After inserting at postion ",pos)
        S.print_LL()
    elif(case==3):
        count=S.length_LL() 
        print("The linked list has length ",count)
    elif(case== 4):
        S.print_mid()
    elif(case== 5):
        S.del_mid()
        print("After Deleting at middle")
        S.print_LL()
    elif(case== 6):
        print("Enter the data")
        val=int(input())
        S.Insert_mid(val)
        print("After inserting at middle")
        S.print_LL()
    elif(case== 7):
        print("The original linked list has ")
        S.print_LL()
        S.remove_duplicates()
        print("After removing duplicates in linked list, it has ")
        S.print_LL()
    elif(case== 8):
        print("Enter the position from end to fetch data")
        pos=int(input())
        print("The original linked list has ")
        S.print_LL()
        S.find_pos_end(pos)
    elif(case== 9):
        print("The original linked list has ")
        S.print_LL()
        S.print_reverse()
        print("After reversing...")
        S.print_LL()
    elif(case==10):
        S.print_LL()
    elif(case==11):
        print("Enter the data")
        val=int(input())
        S.Insert_end(val)
        print("After inserting at end")
        S.print_LL()
    elif(case==12):
        print("Out of list :(")
        break
    else:
        print("Nothing to print :) Try with given option")
