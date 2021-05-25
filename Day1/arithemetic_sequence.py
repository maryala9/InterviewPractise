"""
A sequence of numbers is called arithmetic if it consists of at least two elements,
and the difference between every two consecutive elements is the same.
More formally, a sequence A is arithmetic if and only if A[i+1] - A[i] == A[1] - A[0] for all valid i.
For example, these are arithmetic sequences:
2, 4, 6, 8, 10
9, 9, 9,9
3, -1, -5, -9
The following sequence is not arithmetic:
2, 2, 3, 5, 7
"""


class Solution:
    def check_arithemetic_sequence(self, nums, l, r):
        answers = []
        for (L,R) in zip(l, r):
            subarray = nums[L:R+1]
            subarray = sorted(subarray)
            sequence_flag = True

            for j in range( 1, len(subarray)):
                if subarray[j] - subarray[j-1] != subarray[1] - subarray[0]:
                    sequence_flag = False
                    break
            answers.append(sequence_flag)

        return answers
