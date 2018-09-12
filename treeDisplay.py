import Queue
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left    # left child
        self.right = right  # right child


def levelTraverse(root):
    q = Queue.Queue()
    out = [[]]
    if root:
        q.put(root)
        cur_last = root
        next_last = root
        while not q.empty():
            cur = q.get()
            # print 'now: ', cur.value
            out[-1].append(cur.value)
            if cur.left:
                q.put(cur.left)
                next_last = cur.left
            if cur.right:
                q.put(cur.right)
                next_last = cur.right
            if cur == cur_last:
                out.append([])
                cur_last = next_last
    out.pop()
    return out

def getSize(self):
    if self.left and self.right:
        return 1 + getSize(self.left) + getSize(self.right)
    elif self.left:
        return 1 + getSize(self.left)
    elif self.right:
        return 1 + getSize(self.right)
    else:
        return 1


if __name__ == '__main__':
    n1 = Node(0, None, None)
    n2 = Node(1, n1, None)
    n4 = Node(4, None, None)
    n5 = Node(6, None, None)
    n3 = Node(5, n4, n5)
    head = Node(3, n2, n3)

    print '----LYM_begin----'
    out = [[]]
    print levelTraverse(head)
    print '----LYM_end----'

