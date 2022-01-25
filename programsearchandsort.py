# KVCC 
# CIS-226-23199
# Advanced Python Programming
# 01/25/2022

class customlinkedlist:
    def __init__(self, value, nextnode=None):
        self.value = value
        self.nextnode = nextnode
        
node1 = customlinkedlist("1")
node2 = customlinkedlist("7")
node3 = customlinkedlist("4")
node4 = customlinkedlist("2")
node5 = customlinkedlist("9")
node6 = customlinkedlist("8")
node7 = customlinkedlist("10")
node8 = customlinkedlist("-4")
node9 = customlinkedlist("0")
node10 = customlinkedlist("3")

node1.nextnode = node2
node2.nextnode = node3
node3.nextnode = node4
node4.nextnode = node5
node5.nextnode = node6
node6.nextnode = node7
node7.nextnode = node8
node9.nextnode = node10

def linear_search(customlinkedlist, look_for):
    for i, value in enumerate(customlinkedlist):
        if value == look_for:
            return i
        return -1
index = linear_search(customlinkedlist, 8)
print("The value {} is at index {}".format(8,index))
