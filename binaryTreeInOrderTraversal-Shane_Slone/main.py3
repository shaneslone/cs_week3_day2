#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def binaryTreeInOrderTraversal(root):
    result = []
    def in_order(n):
        if n is None:
            return
        in_order(n.left)
        result.append(n.value)
        in_order(n.right)
    in_order(root)
    return result

