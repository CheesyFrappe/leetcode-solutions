# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        count = 0

        while fast:
            fast = fast.next
            count += 1
        
        print(count)
        count = count // 2
        while count != 0:
            slow = slow.next
            count -= 1
        return slow
