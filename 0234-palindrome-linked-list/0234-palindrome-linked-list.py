# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Time O (N) Space: O (N) Solution
        tmp = []

        while head:
            tmp.append(head.val)
            head = head.next
        
        return tmp == list(reversed(tmp))