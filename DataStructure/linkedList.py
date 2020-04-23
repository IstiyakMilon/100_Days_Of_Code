# A simple Python program for traversal of a linked list 
  
# Node class 
class Node:
  def __init__(self, data):
    self.data=data # Assign data 
    self.next=None 


# Linked List class contains a Node object
class LinkedList:
  def __init__(self):
    self.head=None
  
  # This function prints contents of linked list 
  # starting from head 
  def displayList(self):
    current=self.head
    while(current):
      print(current.data)
      current=current.next


# Start with the empty list 
lList=LinkedList()
# Inserting first node and head pointing to the node 
lList.head=Node(1)
#Creating 2nd node
second=Node(2)
#Creating 3rd node
third=Node(3)
# Link first node with second 
lList.head.next=second
# Link second node with the third node
second.next=third
#  Printing node of the list
lList.displayList()