#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        return self.queue.pop(0)
    def isEmpty(self):
        return self.queue == []
def traverseTree(t):
    queue = Queue()
    result = []
    queue.enqueue(t)
    while not queue.isEmpty():
        cur = queue.dequeue()
        if cur is None:
            continue
        result.append(cur.value)
        queue.enqueue(cur.left)
        queue.enqueue(cur.right)
    return result

