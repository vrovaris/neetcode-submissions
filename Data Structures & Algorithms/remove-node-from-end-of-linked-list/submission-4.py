# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        total = 0
        count = 0

        while (curr != None):
            total += 1
            curr = curr.next

        curr = head

        while (curr != None):
            if count == total - n: 
                if prev == None:
                    head = curr.next 
                    return head
                # elif curr.next == None:
                #     prev.next = None
                #     return head
                else:
                    prev.next = curr.next 
                    curr.next = None
                    return head

            prev = curr
            curr = curr.next
            count += 1

        return head
