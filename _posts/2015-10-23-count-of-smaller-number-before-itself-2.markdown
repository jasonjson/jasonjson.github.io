---
layout: post
title: 249 - Count of Smaller Number before itself
date: 2015-10-23 19:46:11.000000000 -04:00
tags:
- Lintcode
categories:
- Binary Search Tree
author: Jason
---
**Give you an integer array (index from 0 to n-1, where n is the size of this array, value from 0 to 10000) . For each element Ai in the array, count the number of element before this element Ai is smaller than it and return count number array.**


``` java
public class Solution {
   /**
     * @param A: An integer array
     * @return: Count the number of element before this element 'ai' is
     *          smaller than it and return count number array
     */
    class segmentTreeNode {
        int start, end, count;
        segmentTreeNode left, right;
        segmentTreeNode(int start, int end, int count) {
            this.start = start;
            this.end = end;
            this.count = count;
            left = null;
            right = null;
        }
    }
    public ArrayList<Integer> countOfSmallerNumberII(int[] A) {
        // write your code here
        ArrayList<Integer> result = new ArrayList<Integer>();

        segmentTreeNode root = build(0, 10000);
        for (int i = 0; i < A.length; i++) {
            result.add(query(root, 0, A[i] - 1));
            update(root, A[i]);
        }
        return result;
    }
    public segmentTreeNode build(int start, int end) {
        if (start > end) return null;
        if (start == end) return new segmentTreeNode(start, end, 0);
        int mid = (start + end) / 2;
        segmentTreeNode root = new segmentTreeNode(start, end, 0);
        root.left = build(start, mid);
        root.right = build(mid + 1, end);
        root.count = root.left.count + root.right.count;
        return root;
    }

    public int query(segmentTreeNode root, int start, int end) {
        if (root == null) return 0;
        if (root.start == start && root.end == end) return root.count;
        int mid = (root.start + root.end) / 2;
        if (end < mid) {
            return query(root.left, start, end);
        } else if (start > end) {
            return query(root.right, start, end);
        } else {
            return query(root.left, start, mid) + query(root.right, mid + 1, end);
        }
    }

    public void update(segmentTreeNode root, int val) {
        if (root == null || root.start > val || root.end < val) return;
        if (root.start == val && root.end == val) {
            root.count ++;
            return;
        }
        int mid = (root.start + root.end) / 2;
        if (val <= mid) {
            update(root.left, val);
        } else {
            update(root.right, val);
        }
        root.count = root.left.count + root.right.count;
    }
}
```

``` python
class Solution:
    """
    @param: A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def countOfSmallerNumberII(self, A):
        # write your code here

        sort, ret = [], []
        for num in A:
            index = self.query(sort, num)
            sort.insert(index, num)
            ret.append(index)
        return ret

    def query(self, sort, num):
        lo, hi = 0, len(sort) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if sort[mid] == num:
                while mid - 1 >= 0 and sort[mid - 1] == num:
                    mid -= 1
                return mid
            elif sort[mid] > num:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
```
