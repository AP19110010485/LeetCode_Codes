# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return None                    # <-- initialze new lists and dismiss the edge case 
        less, more = ListNode(), ListNode()
        lNode, mNode = less, more
        
        while head :                                # <-- build the two linked lists                  
            if head.val < x :
                lNode.next = head
                lNode = lNode.next
            else:
                mNode.next = head
                mNode = mNode.next
            head=head.next

        lNode.next, mNode.next = more.next, None    # <-- attach more to less

        return less.next   
        