# !/usr/bin/env python
# -*- coding:utf-8 -*-
# time: 2020-04-11 00:03:32
# 描述: K 个一组翻转链表


class LsitNode:

    def __init__(self, x):
        self.value = x
        self.next = None


class Solution:

    def reverseKGroups(self, head, k):

    def reverse(self, start, end):
        pre, cur, nexts = None, start, start
        # 三个指针记性局部翻转
        while cur != end:
            nexts = nexts.next
            # 箭头反指
            cur.next = pre
            # 更新pre位置
            pre = cur
            # 更新cur位置
            cur = nexts

        return pre
