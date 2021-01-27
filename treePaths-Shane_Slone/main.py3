#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def treePaths(t):
    result = []
    def printPath(n, path):
        if n is None:
            return
        if n is t:
            currentPath = str(n.value)
        else:
            currentPath = path + "->" + str(n.value)
        if not n.left and not n.right:
            result.append(currentPath)
            return
        printPath(n.left, currentPath)
        printPath(n.right, currentPath)
    printPath(t, "")
    return result
        

