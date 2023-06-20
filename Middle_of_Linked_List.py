# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Set pointers equal to head for the end pointer and middle pointer.
        middle = head
        end = head

        # Set a while loop to loop through linked list. For every iteration middle will move one and end will move two. Effectively finding the second middle node and the end node
        while end and end.next:
            middle = middle.next
            end = end.next.next

        return middle