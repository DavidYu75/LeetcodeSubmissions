# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # n = 4
        # 1st node = (4-1-1) = 2    (twin of the 2nd node)
        # 3rd node = (4-1-3) = 0    (twin of the 0th node)

        # hashmap that will contain the index key mapped to the node value 
        # go through the linkedlist and map each index with the node value

        # go through the hasmap and calculate the twin values of each node
        # compare it with a max value

        # index_value = {}
        # i = 0
        # length = 0
        # curr = head
        # max_sum = float("-inf")

        # while curr:
        #     index_value[i] = curr.val
        #     curr = curr.next
        #     i += 1
        #     length += 1
        
        # for index in index_value:
        #     twin_node = length - 1 - index

        #     twin_sum = index_value[index] + index_value[twin_node]
        #     max_sum = max(twin_sum, max_sum)
        
        # return max_sum

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        result = 0
        first, second = head, prev
        while second:
            result = max(first.val + second.val, result)
            second = second.next
            first = first.next
        
        return result
            