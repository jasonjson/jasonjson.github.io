#!/usr/bin/python
# -*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        if isinstance(x, list):
            self.val = x[0]
            curr = self
            for i in xrange(1, len(x)):
                curr.next = ListNode(x[i])
                curr = curr.next
            curr.next = None
        else:
            self.val = x
            self.next = None
    def __repr__(self):
        curr = self
        ret = []
        while curr:
            ret.append(str(curr.val))
            curr = curr.next
        return "->".join(ret)
