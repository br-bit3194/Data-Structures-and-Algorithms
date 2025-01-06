'''
Problem Description

Given an array A of N numbers, you have to perform B operations. In each operation, you have to pick any one of the N elements and add the original value(value stored at the index before we did any operations) to its current value. You can choose any of the N elements in each operation.







Perform B operations in such a way that the largest element of the modified array(after B operations) is minimized.
Find the minimum possible largest element after B operations.









Problem Constraints

1 <= N <= 104
0 <= B <= 104
1 <= A[i] <= 104



Input Format

The first argument is an integer array A.
The second argument is an integer B.



Output Format

Return an integer denoting the minimum possible largest element after B operations.



Example Input

Input 1:

 A = [1, 2, 3, 4] 
 B = 3
Input 2:

 A = [5, 1, 4, 2] 
 B = 5


Example Output

Output 1:

 4
Output 2:

 5


Example Explanation

Explanation 1:

 Apply operation on element at index 0, the array would change to [2, 2, 3, 4]
 Apply operation on element at index 0, the array would change to [3, 2, 3, 4]
 Apply operation on element at index 0, the array would change to [4, 2, 3, 4]
 Minimum possible largest element after 3 operations is 4.
Explanation 2:

 Apply operation on element at index 1, the array would change to [5, 2, 4, 2]
 Apply operation on element at index 1, the array would change to [5, 3, 4, 2]
 Apply operation on element at index 1, the array would change to [5, 4, 4, 2]
 Apply operation on element at index 1, the array would change to [5, 5, 4, 2]
 Apply operation on element at index 3, the array would change to [5, 5, 4, 4]
 Minimum possible largest element after 5 operations is 5.

'''

import heapq
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        my_heap = []
        max_val = A[0]
        for element in A:
            max_val = max(max_val, element)
            heapq.heappush(my_heap, (element+element, element))

        for _ in range(B):
            val, original = heapq.heappop(my_heap)
            max_val = max(max_val, val)
            heapq.heappush(my_heap, (val+original, original))
        return max_val

