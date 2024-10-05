class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self) -> None:
        self.start=None
    
    def insertLast(self,value):
        NewNode=Node(value)

        if self.start is None:
            self.start=NewNode

        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=NewNode
    
    def deleteLast(self):
        if self.start is None:
            print('The list is already empty')
            
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next:
                temp=temp.next
            temp.next=None

    def deleteFirst(self):
        if self.start==None:
            print("The list is already empty")
        else:
            self.start=self.start.next

        
    def vewList(self):
        if self.start is None:
            print('The list is Empty!')
        
        else:
            temp=self.start
            while temp is not None:
                print(temp.data, end=' ')
                temp=temp.next
            

L_list=LinkedList()

L_list.insertLast(10)
L_list.insertLast(9)
L_list.insertLast(30)
L_list.insertLast(39)
L_list.insertLast(93)
L_list.insertLast(83)

L_list.deleteLast()
L_list.deleteFirst()

L_list.vewList()


