class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
      if head==None:
        new_node = Node(data)
        head = new_node
      elif head.next==None:
        new_node=Node(data)
        head.next=new_node
      else:
        self.insert(head.next,data)
      return head
 
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  