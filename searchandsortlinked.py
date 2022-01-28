class Node:#Singly Linked List
    def __init__(self, data, next=None):
        self.data = data
        self.next = next#Next item in the list
        
            
def linear_search(node, look_for):
    while node:
        
        node = look_for
        node(node.next)
        
    
        if not node:
            break
                   
    
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

node1.nextnode = node2
node2.nextnode = node3
node3.nextnode = node4
node4.nextnode = node5
node5.nextnode = node6
node6.nextnode = node7
node7.nextnode = node8
node9.nextnode = node10



           
            

            
        

    