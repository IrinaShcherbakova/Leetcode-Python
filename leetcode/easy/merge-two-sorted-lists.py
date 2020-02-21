# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = []
        list = None
        headFirst = l1
        headSecond = l2
        while headFirst != None and headSecond != None:
            if headFirst.val < headSecond.val:
                res.append(headFirst.val)
                headFirst = headFirst.next
            else:
                res.append(headSecond.val)
                headSecond = headSecond.next
        while headSecond:
            res.append(headSecond.val)
            headSecond = headSecond.next
        while headFirst:
            res.append(headFirst.val)
            headFirst = headFirst.next
        print(res)
        if len(res) > 0:
            previous = current = None
            for node in res:
                current = ListNode(node)
                if previous:
                    previous.next = current
                if not list:
                    list = current
                previous = current
        return list

