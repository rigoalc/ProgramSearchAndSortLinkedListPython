class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
    def traverse(self):
        print("{} -> ".format(self.data),end='')
        if self.next:
            self.next.traverse()
        else:
            print('NULL')
def traverse_linked_list(node):
    if not node:
        print('NULL')
        return
    print("{} -> ".format(node.data), end='')
    traverse_linked_list(node.next)
    
            
            
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


traverse_linked_list(node1) 
node1.traverse()           
            

            
        

    