# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        currentA = headA
        currentB = headB

        while currentA:
            visited.add(currentA)
            currentA = currentA.next

        while currentB:
            if currentB in visited:
                return currentB
            currentB = currentB.next
        
        return None
