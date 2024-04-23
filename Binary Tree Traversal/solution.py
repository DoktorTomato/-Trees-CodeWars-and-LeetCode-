'''
This script has function that help traversing the tree
'''

class Node:
    '''
    This is a class for node
    '''
    def __init__(self, data, left_data=None, right_data=None) -> None:
        self.data = data
        self.left = left_data
        self.right = right_data

# Pre-order traversal
def pre_order(node):
    '''
    This function traverses the tree in pre-order
    '''
    res = []
    if node is None or node.data is None:
        return res
    res.append(node.data)
    if node.left is not None:
        res.extend(pre_order(node.left))
    if node.right is not None:
        res.extend(pre_order(node.right))
    return res

# In-order traversal
def in_order(node):
    '''
    This function traverses the tree in in-order
    '''
    res = []
    if node is None or node.data is None:
        return res
    if node.left is not None:
        res.extend(in_order(node.left))
    res.append(node.data)
    if node.right is not None:
        res.extend(in_order(node.right))
    return res

# Post-order traversal
def post_order(node):
    '''
    This function traverses the tree in post-order
    '''
    res = []
    if node is None or node.data is None:
        return res
    if node.left is not None:
        res.extend(post_order(node.left))
    if node.right is not None:
        res.extend(post_order(node.right))
    res.append(node.data)
    return res

if __name__ == '__main__':
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")

    a.left = b
    a.right = c
    c.left = d

    print(post_order(a))
