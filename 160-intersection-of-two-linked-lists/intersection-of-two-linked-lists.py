# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currentA = headA
        currentB = headB

        visited = set()

        while currentA:
            visited.add(currentA)
            currentA = currentA.next
        
        while currentB:
            if currentB in visited:
                return currentB
            currentB = currentB.next
        
        return None

        # currentA = headA
        # currentB = headB

        # while currentA != currentB:
        #     currentA = headB if currentA is None else currentA.next
        #     currentB = headA if currentB is None else currentB.next
        
        # return currentA
