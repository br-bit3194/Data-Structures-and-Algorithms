'''
Problem Description
There is a row of seats represented by string A. Assume that it contains N seats adjacent to each other.
There is a group of people who are already seated in that row randomly. i.e. some are sitting together & some are scattered.

An occupied seat is marked with a character 'x' and an unoccupied seat is marked with a dot ('.')

Now your target is to make the whole group sit together i.e. next to each other, without having any vacant seat between them in such a way that the total number of hops or jumps to move them should be minimum.

In one jump a person can move to the adjacent seat (if available).

NOTE: 1. Return your answer modulo 107 + 3.



Problem Constraints
1 <= N <= 1000000
A[i] = 'x' or '.'



Input Format
The first and only argument is a string A of size N.



Output Format
Return an integer denoting the minimum number of jumps required.



Example Input
Input 1:

 A = "....x..xx...x.."
Input 2:

 A = "....xxx"


Example Output
Output 1:

 5
Output 2:

 0

'''

class Solution:
	# @param A : string
	# @return an integer
	def seats(self, A):
        positions = []
        OCCUPIED = 'x'
        for index,seat in enumerate(A):
            if seat==OCCUPIED:
                positions.append(index)
        
        mid_position = 0
        mod = 10**7+3
        occupied_seats = len(positions)

        if occupied_seats==len(A) or occupied_seats==0:
            return 0

        if occupied_seats%2!=0:
            mid_position = positions[occupied_seats//2]
        else:
            mid_position = (positions[occupied_seats//2]+positions[(occupied_seats+1)//2])//2
        # return mid_position
        less_index = 1
        higher_index = 1
        total_hopes = 0
        for pos in positions:
            diff = abs(pos-mid_position)
            if diff>0:
                if pos<mid_position:
                    diff-=less_index
                    less_index+=1
                else:
                    diff-=higher_index
                    higher_index+=1
            total_hopes += diff%mod
            total_hopes %= mod
        return total_hopes


