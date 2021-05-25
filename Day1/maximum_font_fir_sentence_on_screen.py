#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
#
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """

class Solution:
    def maxFont(self, text, w, h, fonts, fontInfo):
        def check(fs):
            if fontInfo.getHeight(fs) > h:
                return False
            if sum(fontInfo.getWidth(fs, c) for c in text) > w:
                return False

            return True

        l = 0
        r = len(fonts) - 1
        while l < r:
            mid = (l + r) //2
            if check(fonts[mid + 1]):
                l = mid + 1
            else:
                r = mid
        return fonts[l] if check(fonts[l]) else -1
