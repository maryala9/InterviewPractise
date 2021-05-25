class Solution:
    def numberOfSubstrings(self, s):
        res = 0
        start = 0
        count = {c: 0 for c in 'abc'}
        for end in range(len(s)):
            count[s[end]] += 1
            while all(count.values()):
                count[s[start]] -= 1
                start += 1
            res += start

        return res
