"""
This module contains a solution for a LeetCode Problem "21. Merge Two Sorted Lists":
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

@author: Olga Aleksandrova
@licence: MIT
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
       :type list1: Optional[ListNode]
       :type list2: Optional[ListNode]
       :rtype: Optional[ListNode]
    """
    final_list_head = cur_list_head = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            cur_list_head.next = list1
            list1 = list1.next
        else:
            cur_list_head.next = list2
            list2 = list2.next
        cur_list_head = cur_list_head.next
    if list1:
        cur_list_head.next = list1
    elif list2:
        cur_list_head.next = list2

    return final_list_head.next


#print(merge_two_lists(ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}},
#ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}))