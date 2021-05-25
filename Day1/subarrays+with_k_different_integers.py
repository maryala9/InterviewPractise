import collections
class Solution:
    def subarraysWithKDistinct(self, nums, k):
        # since this is subarrays and k distinct - sliding window question
        # atmost(k) times = atmost(k) times - atmost(k-1) times

        def atMost(nums, k):
            res = 0
            start = 0
            count = collections.Counter()
            for end in range(len(nums)):
                if count[nums[end]] == 0:
                    k -= 1
                count[nums[end]] += 1
                while k < 0:
                    count[nums[start]] -= 1
                    if count[nums[start]] == 0:
                        k += 1
                    start += 1
                res += end - start + 1
            return res

        return atMost(nums, k) - atMost(nums, k-1)



