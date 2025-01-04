"""
Problem Description

Given a list containing head pointers of N sorted linked lists.
Merge these given sorted linked lists and return them as one sorted list.



Problem Constraints

1 <= total number of elements in given linked lists <= 100000



Input Format

The first and only argument is a list containing N head pointers.



Output Format

Return a pointer to the head of the sorted linked list after merging all the given linked lists.



Example Input

Input 1:

 1 -> 10 -> 20
 4 -> 11 -> 13
 3 -> 8 -> 9
Input 2:

 10 -> 12
 13
 5 -> 6


Example Output

Output 1:

 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
Output 2:

 5 -> 6 -> 10 -> 12 ->13


Example Explanation

Explanation 1:

 The resulting sorted Linked List formed after merging is 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20.
Explanation 2:

 The resulting sorted Linked List formed after merging is 5 -> 6 -> 10 -> 12 ->13.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        li = []
        head = None
        tail = None
        for r in range(len(A)):
            heapq.heappush(li, (A[r].val, r, A[r]))
        
        while(li):
            val, r, pnt = heapq.heappop(li)
            if head==None:
                head = pnt
                tail = head
            else:
                tail.next = pnt
                tail = tail.next
            
            if pnt.next:
                pnt = pnt.next
                heapq.heappush(li, (pnt.val, r, pnt))
        return head