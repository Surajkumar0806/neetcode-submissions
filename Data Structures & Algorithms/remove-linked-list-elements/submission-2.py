# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head 
        while head and head.val == val:
            head = head.next
        current = head 
        while current:
            temp = current.next
            while temp and temp.val == val:
                current.next = temp.next
                temp = current.next
            current = current.next 
        return head 