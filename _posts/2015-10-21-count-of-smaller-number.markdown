---
layout: post
title: 248 - Count of Smaller Number
date: 2015-10-21 13:32:46.000000000 -04:00
tags:
- Leetcode
categories:
- Array
author: Jason
---
**Give you an integer array (index from 0 to n-1, where n is the size of this array, value from 0 to 10000) and an query list. For each query, give you an integer, return the number of element in the array that are smaller that the given integer.**


``` java
public class Solution {
   /**
     * @param A: An integer array
     * @return: The number of element in the array that
     *          are smaller that the given integer
     */

    class segmentTreeNode {
        int start, end, count;
        segmentTreeNode left, right;
        segmentTreeNode(int start, int end, int count) {
            this.start = start;
            this.end = end;
            this.count = count;
            this.left = null;
            this.right = null;
        }
    }
    public ArrayList<Integer> countOfSmallerNumber(int[] A, int[] queries) {
        // write your code here
        ArrayList<Integer> result = new ArrayList<Integer>();

        segmentTreeNode root = build(0, 10000);
        for (int n : A) {
            update(root, n);
        }
        for (int n : queries) {
            result.add(query(root, 0, n - 1));
        }
        return result;
    }

    public segmentTreeNode build(int start, int end) {
        if (start > end) return null;
        if (start == end) return new segmentTreeNode(start, end, 0);//base case
        segmentTreeNode root = new segmentTreeNode(start, end, 0);
        int mid = (start + end) / 2;
        root.left = build(start, mid);
        root.right = build(mid + 1, end);
        root.count = root.left.count + root.right.count;
        return root;
    }
    public int query(segmentTreeNode root, int start, int end) {
        if (start > end) return 0;
        if (root.start == start && root.end == end) return root.count;
        int mid = (root.start + root.end) / 2;
        if (end < mid) {
            return query(root.left, start, end);
        } else if (start > mid) {
            return query(root.right, start, end);
        } else {
            return query(root.left, start, mid) + query(root.right, mid + 1, end);
        }
    }
    public void update(segmentTreeNode root, int val) {
        if (root == null) return;
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
    @param: A: An integer array
    @param: queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here

        A.sort()
        return [self.query(A, num) for num in queries]

    def query(self, A, target):
        lo, hi = 0, len(A) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if A[mid] == target:
                while mid - 1 >= 0 and A[mid - 1] == target:
                    mid -= 1
                return mid
            elif A[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
```
