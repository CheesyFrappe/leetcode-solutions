# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        
        count = 0
        while count != n:
            fast = fast.next
            count += 1
        
        if not fast:
            head = head.next
            return head  
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        if slow.next.next:
            slow.next = slow.next.next
        else:
            slow.next = None
        return head 

