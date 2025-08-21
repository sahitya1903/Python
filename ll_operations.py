class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def delete_first(self):
        if not self.head:
            return
        temp=self.head.data
        self.head=self.head.next
        return temp
    
    def delete_last(self):
        temp=self.head
        data=self.head.data
        if not temp:
            return
        if not temp.next:
            temp.next=None
            return data
        
        while temp.next.next:
            temp=temp.next
        temp.next=None
        return data

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    ll.print_list()
    ll.delete_with_value(0)
    ll.print_list()
    ll.delete_first()
    ll.print_list()
    ll.delete_last()
    ll.print_list()

