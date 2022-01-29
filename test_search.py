from searchandsortlinked import Node, find_midway

def test_find_midway():
    
    node1 = Node('1')
    node2 = Node('2')
    node3 = Node('3')
    
    node1.next = node2
    node2.next = node3
      
    
    node2.prev = node1
    node3.prev = node2
    
    assert find_midway(node1, node3) == node2
    
    
    