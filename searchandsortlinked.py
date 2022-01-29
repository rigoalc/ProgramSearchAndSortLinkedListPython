class Node:#Class to define Nodes
   
    def __init__(self, data, prev=None, next=None):#Function for define variables
        self.data = data
        self.next = next#Next item in the list
        self.prev = prev#Prev item in the list
        
    def __str__(self):
        return "{}".format(self.data)

def traverse_linked_list(node):#Function to traverse the list 
    """Print out nodes recursively"""
    if not node: # Base Case
        print('NULL') # Adds newline
        return
    print("{} -> ".format(node.data), end='') # Set end='' to not do newline
    # Do next node
    traverse_linked_list(node.next)
        
            
def linear_search(node, look_for):#Function for linear search in the linked list
    iteration = 0
    while node:
        if node.data == look_for:
            print(node.data)
            print("This took:", iteration,"steps.")
            return
        node = node.next
        iteration += 1
    print("Not Found")
    
def insertion_sort(node):#Function for insertion sort
    iteration = 0
    marker_a = node.next   
    while marker_a:
        unsorted_value = marker_a.data
        marker_b = marker_a
        while marker_b.prev and marker_b.prev.data > unsorted_value:
            marker_b.data = marker_b.prev.data  
            marker_b = marker_b.prev
            iteration += 1
        marker_b.data = unsorted_value
        marker_a = marker_a.next
    head = node
    while head.prev:
        head = head.prev
    traverse_linked_list(head)
    print("This took:", iteration,"steps.")
    
def binary_search(node, look_for):
        marker_a = 0
        marker_b = marker_a
        iteration = 0
        while  marker_b < marker_b.next.data:
            marker_b = marker_a
                
               
node1 = Node("1")
node2 = Node("7")
node3 = Node("4")
node4 = Node("2")
node5 = Node("9")
node6 = Node("8")
node7 = Node("10")
node8 = Node("-4")
node9 = Node("0")
node10 = Node("3")

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10

node2.prev = node1
node3.prev = node2
node4.prev = node3
node5.prev = node4
node6.prev = node5
node7.prev = node6
node8.prev = node7
node9.prev = node8
node10.prev = node9




           
            

            
        

    