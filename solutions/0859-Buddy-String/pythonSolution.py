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

    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        cycle_index = 0
        different_index = []
        same_alpha = 0
        while cycle_index < len(A):
            if A.find(A[cycle_index], cycle_index + 1) > 0:
                same_alpha += 1
            if len(different_index) > 2:
                return False
            if A[cycle_index] != B[cycle_index]:
                different_index.append(cycle_index)
            cycle_index += 1
        if len(different_index) == 0 and same_alpha > 0:
            return True
        if len(different_index) != 2:
            return False
        new_string = A[:different_index[0]] + A[different_index[1]] + \
                     A[different_index[0] + 1:different_index[1]] + A[different_index[0]] + A[different_index[1] + 1:]
        if new_string != B:
            return False
        return True

    def best_solution(self, A, B):
        if len(A) != len(B) or set(A) != set(B): return False
        if A == B:
            return len(A) - len(set(A)) >= 1
        else:
            indices = []
            counter = 0
            for i in range(len(A)):
                if A[i] != B[i]:
                    counter += 1
                    indices.append(i)
                if counter > 2:
                    return False
            return A[indices[0]] == B[indices[1]] and A[indices[1]] == B[indices[0]]


if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.best_solution("ac", "ac"))
