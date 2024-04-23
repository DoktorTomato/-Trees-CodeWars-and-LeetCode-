'''
This script has a function that traverses a tree by levels
'''

class Node:
    '''
    This is a Node class
    '''
    def __init__(self, left, right, data):
        self.left = left
        self.right = right
        self.value = data

def tree_by_levels(node):
    '''
    This function takes a tree node as an argument and
    returns a list of values in level by level style
    '''
    res = []
    if node:
        queue = [node]
        while len(queue) != 0:
            res.append(queue[0].value)
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            queue.pop(0)
    return res
