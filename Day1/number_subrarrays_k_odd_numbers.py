class Solution:
    def number_of_subarrays_k_odd_integers(self, nums, k):
        # res = 0
        # count = 0
        # start = 0
        # for end in range(len(nums)):
        #     if nums[end] & 1:
        #         k -= 1
        #         count = 0
        #     while k == 0:
        #         k += nums[start] & 1
        #         start += 1
        #         count += 1
        #     res += count
        # return res
#         number of Subbarrays is always about finding atmost(k) times  = atmost(k) times - atmost(k-1) times
        def atMost(k):
            res = 0
            start = 0

            for end in range(len(nums)):
                k -= end % 2
                while k < 0:
                    k += nums[start] % 2
                    start += 1
                res += end - start + 1
            return res


        return atMost(k) - atMost(k-1)




print(Solution().number_of_subarrays_k_odd_integers([2,2,2,1,2,2,1,2,2,2], 2))