class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def concat(self, L):
        last=self.tail.prev
        start=L.head.next
        last.next=start
        start.prev=last
        self.tail=L.tail
        self.nodeCount += L.nodeCount

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        curr=prev.next
        next=curr.next
        prev.next=next
        next.prev=prev
        self.nodeCount-=1
        return curr.data


    def popBefore(self, next):
        curr=next.prev
        prev=curr.prev
        prev.next=next
        next.prev=prev
        self.nodeCount-=1
        return curr.data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        else:
            return self.popBefore(pos+1)

def solution(x):
    return 0


a1=Node(1)
a2=Node(2)
a3=Node(3)
b1=Node(1)
b2=Node(2)
b3=Node(3)

L1=DoublyLinkedList()
L2=DoublyLinkedList()
L1.insertAt(1,a1)
L1.insertAt(2,a2)
L1.insertAt(3,a3)

L2.insertAt(1,b3)
L2.insertAt(2,b2)
L2.insertAt(3,b1)
L1.concat(L2)
print(L1.traverse())
print(L2.traverse())