"""
This module contains a solution for a LeetCode Problem "206. Reverse Linked List":
Given the head of a singly linked list, reverse the list, and return the reversed list.

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

@author: Olga Aleksandrova
@licence: MIT
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    current_pointer = head
    new_next = None  # next node in reverse list (after the head)
    while current_pointer:
        forward_next = current_pointer.next  # remember next node in forward direction
        current_pointer.next = new_next  # switching direction (next Node for reverse list)
        new_next = current_pointer
        current_pointer = forward_next
    return new_next
