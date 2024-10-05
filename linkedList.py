# creating node 
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.start=None

    def insertLast(self,value):         # insert element at the last of the linked list
        newNode=Node(value)        # creating new node

        if self.start is None:          
            self.start=newNode
        else:
            temp=self.start         # initialize starting address to temp for traversing
            while temp.next is not None:
                temp=temp.next
            
            # now temp is the last node
            temp.next=newNode   #new node is assign to last
        print('\nNew node inserted\n')


    #delete first node
    def deleteFirst(self):

        if self.start is None:
            print('\nLinked list is empty\n')

        else:
            # first starting address is not assign to any tempory veriable for deletion because, in python there is dynamically deletion 
            # we do not need to delete. pyhton delete the memory content that is not reffer by any variable
            self.start=self.start.next
            print('\nFirst node is deleted\n')


    #show the list
    def viewList(self):
        
        if self.start is None:
            print('\nThere is no node to print\n')
        else:
            temp=self.start
            while temp is not None:
                print(temp.data,end=' ')
                temp=temp.next


myList=LinkedList()
myList.insertLast(10)
myList.insertLast(16)
myList.insertLast(102)
myList.insertLast(15)
myList.insertLast(14)
myList.insertLast(13)

myList.viewList()
myList.deleteFirst()
myList.viewList()