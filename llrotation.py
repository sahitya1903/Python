class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotate_right(head, k):
    if not head or not head.next or k == 0:
        return head
    
    # Compute the length of the list
    length = 1
    temp = head
    while temp.next:
        temp = temp.next
        length += 1
    
    # Connect the tail to head to make it circular
    temp.next = head
    
    # Find the new head position
    k = k % length
    skip = length - k
    temp = head
    for _ in range(skip - 1):
        temp = temp.next
    
    # Break the loop and set the new head
    new_head = temp.next
    temp.next = None
    
    return new_head

def print_list(head):
    temp = head
    while temp:
        print(temp.val, end=" -> ")
        temp = temp.next
    print("None")

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    
    print("Original List:")
    print_list(head)
    
    k = 2
    head = rotate_right(head, k)
    
    print(f"Rotated List by {k} positions:")
    print_list(head)
