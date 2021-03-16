""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    min_left = -9999999
    max_right = 9999999
    def check(node, left, right):
        if node is None:
            return True
        if node.data <= left:
            return False
        if node.data >= right:
            return False
        return check(node.left, left, node.data) and check(node.right, node.data, right)
    
    return check(root, min_left, max_right)
