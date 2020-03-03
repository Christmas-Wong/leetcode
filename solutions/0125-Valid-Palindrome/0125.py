#!/usr/bin/env python
# encoding: utf-8
"""
@author: WangFei
@license: (C) Copyright 2013-2020, Node Supply Chain Manager Corporation Limited.
@contact: wf18684531169@gmail.com
@software: pycharm
@file: leetcode.py
@time: 2020/3/2 23:12
@desc
"""
class Solution(object):
    def is_palindrome_double_pointer(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s_len = len(s)
        start_pointer = 0
        end_pointer = s_len-1
        while start_pointer <= end_pointer:
            if not s[start_pointer].isdigit() and not s[start_pointer].isalpha():
                start_pointer += 1
                continue
            if not s[end_pointer].isdigit() and not s[end_pointer].isalpha():
                end_pointer -= 1
                continue
            if s[start_pointer] != s[end_pointer]:
                return False
            start_pointer += 1
            end_pointer -= 1
        return True

    def is_palindrome_stack(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        my_string = s.lower()
        index = 0
        return_value = True
        while index < len(my_string):
            if not my_string[index].isdigit() and not my_string[index].isalpha():
                index += 1
                continue
            stack.append(my_string[index])
            index += 1
        fake_mid = int(len(stack)/2)
        real_mid = 0
        if len(stack) % 2 == 0:
            real_mid = fake_mid
        else:
            real_mid = fake_mid + 1
        pop_index = 0
        while pop_index < real_mid:
            if stack[pop_index] != stack.pop():
                return_value = False
            pop_index += 1
        return return_value


if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.is_palindrome_stack("A man, 1a plan, a canal: Panama"))