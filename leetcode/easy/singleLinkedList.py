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
