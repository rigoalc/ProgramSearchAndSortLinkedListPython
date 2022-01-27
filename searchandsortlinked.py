
class Nodes:
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        
class linkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        node = customLikedList(value)
        if self.head is not None:
            self.head = node
            return  
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode