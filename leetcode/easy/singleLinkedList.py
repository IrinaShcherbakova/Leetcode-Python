# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def hasCycle(self, head) -> bool:
        if head is None:
            return False
        slowPointer = head
        fastPointer = head.next
        while fastPointer is not None:
            if fastPointer == slowPointer:
                return True
            if fastPointer.next is None:
                return False
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
        return False

    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        currentA = headA
        currentB = headB
        lengthA = lengthB = 0
        while currentA is not None:
            lengthA += 1
            currentA = currentA.next
        while currentB is not None:
            lengthB += 1
            currentB = currentB.next
        if lengthA > lengthB:
            longerList = headA
            shorterList = headB
        else:
            longerList = headB
            shorterList = headA
        lengthDif = abs(lengthA - lengthB)
        while lengthDif > 0:
            longerList = longerList.next
            lengthDif -= 1
        print("longer list starts at %s" % longerList.val)
        while longerList is not None:
            if longerList == shorterList:
                return longerList
            longerList = longerList.next
            shorterList = shorterList.next
        return None

