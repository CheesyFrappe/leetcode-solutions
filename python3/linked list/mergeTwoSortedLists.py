"""
    21 - Merge Two Sorted Lists - Easy
    https://leetcode.com/problems/merge-two-sorted-lists/
    Topics: Linked List

    Runtime complexity: O(n + m)
    Spacetime complexity: O(n + m)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

"""
Iterative approach:

Runtime complexity: O(n)
Spacetime complexity: O(1)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = res = ListNode()

        while list1 and list2:
            if list1.val >= list2.val:
                list2, curr.next = list2.next, list2
            else:
                list1, curr.next = list1.next, list1
            curr = curr.next
                  
        if list1 or list2:
            curr.next = list1 if list1 else list2
        
        return res.next

"""
       