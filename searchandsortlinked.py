# Kim Bottomley & Rodrigo Alcover
# Program Search and Sort due 1/29/2022
# CIS 226-23199 Advanced Python Programming
# 20hrs

'''Design: How will you solve the problem? I will solve the problem by writing a program that uses a 
linked list for a linear search, binary search and an insertion sort. 
This program will also count the number of steps it takes to complete each action.

Develop: What did you actually do to solve the problem? I solved the problem by creating a linked list 
then using that list to run a linear search, a binary search and a selection sort. The program also counts how 
many steps it takes to complete each and prints the count at the end.

Test: What did you test? I tested the midway function assert the midway of 3 three nodes and asserting the results.
Document: Explain your code for your future self and others. This program preforms a linear search, 
binary search and a selection sort on a linked list. At the bottom you can change the data in the nodes and also 
which node to search for or start with for the selection sort.

How to use the program: Open the program. You can change the data values for the nodes a the bottom to use different data. 
If you do change the values then you will also want to change the ‘main’ program where it says linear_search and binary_search 
to match the node you are looking for. Hit Run, the program will then print the number of steps it took to complete the searches and sort.
'''

class Node:#Class to define Nodes
   
    def __init__(self, data, prev=None, next=None):#Function for define variables
        self.data = data
        self.next = next
        self.prev = prev
        
    def __str__(self):
        return "{}".format(self.data)

def traverse_linked_list(node):#Function to traverse the list 
    """Print out nodes recursively"""
    if not node: 
        print('NULL') 
        return
    print("{} -> ".format(node.data), end='') # Set end='' to not do newline
    traverse_linked_list(node.next)
        
            
def linear_search(node, look_for):#Function for linear search in the linked list
    ''' O(n)'''
    iteration = 0 
    while node:
        if node.data == look_for:
            print(node.data)
            print("This took:", iteration,"steps to perform linear search.")
            return
        node = node.next
        iteration += 1
    print("Not Found")
    
def insertion_sort(node):#Function for insertion sort
    '''O(n^2)'''
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
    print("This took:", iteration,"steps to perform insertion sort.")
    return head

    
def binary_search(node, look_for):#Function for perform binary search
    '''O(log N)'''
    count = 0
    start = node
    end = node
    while end.next:
        end = end.next
    found = None
    while found is None and start != end.next:
        midway = find_midway(start, end)
        if midway.data == look_for:
            found = midway
        elif midway.data < look_for:
            start = midway.next
        else:
            end = midway.prev
        count += 1
    print ("This took:", count,"steps to perform binary search.")
    
    return found


def find_midway(start, end):#Function for find the midway of the list
    count = 0
    node = start
    while node != end:
        node = node.next
        count += 1
    print(count)
    midway = int(count/2)
    for x in range(midway):
        start = start.next
    return start
                  
node1 = Node(1)
node2 = Node(7)
node3 = Node(4)
node4 = Node(2)
node5 = Node(9)
node6 = Node(8)
node7 = Node(10)
node8 = Node(-4)
node9 = Node(0)
node10 = Node(3)

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

#find_midway(node1, node5)
if __name__ == '__main__':
     
    linear_search(node1, 8)#call linear search function
    head = insertion_sort(node1)#call the intertion sort function
    found = binary_search(head, 8)#call the binary search function
    




           
            

            
        

    