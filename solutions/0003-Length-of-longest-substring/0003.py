class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1:
            return 0
        if len(s) == 1 or len(set(s)) == 1:
            return 1
        set_list = []
        counter = 0
        pointer = 0
        i = 0
        while i < (len(s)):
            if s[i] not in set_list:
                set_list.append(s[i])
            else:
                if len(set_list) > counter:
                    counter = len(set_list)
                index = set_list.index(s[i])
                pointer += index
                set_list = []
                i = pointer
                pointer += 1
            i += 1
        if len(set_list) > counter:
            counter = len(set_list)
        return counter