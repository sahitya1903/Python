class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.head=None

    def append(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        currnode=self.head
        while currnode.next:
            currnode=currnode.next
        currnode.next=newnode

    def prepend(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

    def delete(self,key):
        if self.head is None:
            return
        if self.head.data==key:
            self.head=self.head.next
        currnode=self.head
        while currnode.next:
            if currnode.next.data==key:
                currnode.next=currnode.next.next
                return
            currnode=currnode.next
        
    def reverse(self):
        prev = None
        currnode = self.head
        while currnode:
            next = currnode.next
            currnode.next = prev
            prev = currnode
            currnode = next
        self.head = prev

    def  printlink(self):
        currnode=self.head
        while currnode:
            print(currnode.data,end='-> ')
            currnode=currnode.next
        print('None')


ll=LL()
ll.append(2)
ll.append(3)
ll.append(4)
ll.printlink()
ll.prepend(1)
ll.prepend(0)
ll.printlink()
ll.delete(0)
ll.printlink()
ll.reverse()
ll.printlink()