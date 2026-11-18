# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False
        slow = head
        fast = slow.next

        while (fast != None and slow != None):
            if slow.val == fast.val:
                return True
            else:
                slow = slow.next
                fast = fast.next.next if fast.next != None else fast.next

        return False